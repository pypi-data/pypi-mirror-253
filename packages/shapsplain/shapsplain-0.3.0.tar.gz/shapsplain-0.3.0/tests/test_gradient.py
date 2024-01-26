import shapsplain.importers

tf = shapsplain.importers.import_tensorflow()
np = shapsplain.importers.import_numpy()

from sensenet.preprocess.preprocessor import Preprocessor
from sensenet.models.deepnet import apply_layers
from sensenet.models.settings import Settings

from shapsplain.gradient import GradientExplainer
from shapsplain.utils import make_fields

from .utils import read_gzipped_json, load_numeric_data


def numeric_deepnet(json_model):
    nfeatures = len(json_model["preprocess"])
    raw_inputs = tf.keras.Input((nfeatures,), dtype=tf.float32)
    preprocessor = Preprocessor(json_model, {})
    inputs = preprocessor(raw_inputs)

    predictions = apply_layers(json_model, Settings({}), inputs, None)
    return tf.keras.Model(inputs=raw_inputs, outputs=predictions)


def check_scores(model, X, phis, nclasses, nfeatures):
    preds = model(X).numpy()

    assert len(phis) == nclasses

    for i, phi in enumerate(phis):
        assert tuple(phi.shape) == (X.shape[0], nfeatures + 1)

        diff = preds[:, i] - np.sum(phi, axis=1)

        if nclasses > 1:
            assert np.all(np.abs(diff) < 1e-7), str(diff)
        else:
            # Magnitude of predicted values for yacht is larger
            assert np.all(np.abs(diff) < 1e-5), str(diff)


def check_importances(imps, nfeatures):
    assert len(imps) == nfeatures
    for imp in imps:
        assert len(imp) == 2
        assert type(imp[0]) == str
        assert imp[1] > 0

    0.99999 < sum([imp[1] for imp in imps]) < 1.00001


def test_iris_model():
    nclasses = 3
    nfeatures = 4

    X, y, model_fields = load_numeric_data("tests/data/iris.json.gz")
    vmap = {i: None for i in model_fields}
    fields = make_fields({"model": {"fields": model_fields}}, vmap)

    json_model = read_gzipped_json("tests/data/iris_deepnet.json.gz")
    model = numeric_deepnet(json_model)

    gexp = GradientExplainer(model, X, fields)
    shap_values = gexp.compute_shap(X)
    imps = gexp.shap_importances()

    check_scores(model, X, shap_values, nclasses, nfeatures)
    check_importances(imps, nfeatures)


def test_yacht_model():
    nclasses = 1
    nfeatures = 6

    X, y, model_fields = load_numeric_data("tests/data/yacht.json.gz")
    vmap = {i: None for i in model_fields}
    fields = make_fields({"model": {"fields": model_fields}}, vmap)

    json_model = read_gzipped_json("tests/data/yacht_deepnet.json.gz")
    model = numeric_deepnet(json_model)

    gexp = GradientExplainer(model, X, fields)
    shap_values = gexp.compute_shap(X)
    imps = gexp.shap_importances()

    check_scores(model, X, shap_values, nclasses, nfeatures)
    check_importances(imps, nfeatures)


def test_iris_explanation():
    X, y, model_fields = load_numeric_data("tests/data/iris.json.gz")
    vmap = {i: None for i in model_fields}
    fields = make_fields({"model": {"fields": model_fields}}, vmap)

    json_model = read_gzipped_json("tests/data/iris_deepnet.json.gz")
    model = numeric_deepnet(json_model)

    gexp = GradientExplainer(model, X, fields)
    data = read_gzipped_json("tests/data/iris.json.gz")

    point = {k: v for k, v in zip(data[0], data[1])}
    exp = gexp.predict(point, explanation=True)

    assert len(exp) == 3

    for cls in exp:
        assert len(cls) == 5

        for f in cls[1:]:
            assert len(f) == 2
            assert type(f[1]) == float

    assert exp[0][0] > 0.99
    assert exp[0][1][0] == "2"
    assert exp[0][1][1] > 0.2

    for cls in exp[1:]:
        assert cls[0] < 0.01
        assert cls[1][1] < 0

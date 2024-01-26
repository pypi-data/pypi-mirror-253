import numpy as np

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from shapsplain.utils import to_numpy
from shapsplain.scikit import to_shap_forest, shap_importances

from .original_shap import TreeExplainer
from .utils import load_numeric_data


def sklearn_predictor(X, y, classify):
    if classify:
        predictor = RandomForestClassifier(random_state=0)
    else:
        predictor = RandomForestRegressor(random_state=0)

    predictor.fit(X, y)
    return predictor


def prediction_consistency(datafile, classify):
    X, y, fields = load_numeric_data(datafile)

    predictor = sklearn_predictor(X, y, classify)
    texp = TreeExplainer(predictor)
    sforest = to_shap_forest(predictor, fields)

    for i, row in enumerate(X[:128, :]):
        # It's totally crazy, but this is consistent with scikit
        # and nothing else is.  We're replicating here a cast
        # and loss of precision they do internally somewhere.
        instance = {str(f): np.float64(np.float32(v)) for f, v in enumerate(row)}

        try:
            skpred = predictor.predict_proba([row])[0]
        except AttributeError:
            skpred = predictor.predict([row])

        shappred = sforest.predict(instance)

        assert len(skpred) == len(shappred)
        assert np.sum(np.abs(skpred - shappred)) < 1e-8

        if classify:
            assert np.sum(shappred) == 1

        if i % 32 == 0:
            my_shap = sforest.compute_shap(instance)
            his_shap = texp.shap_values(to_numpy(sforest._fields, instance))

            if classify:
                for mine, his in zip(my_shap, his_shap):
                    assert mine.shape[0] == X.shape[1] + 1
                    assert np.sum(mine - his) == 0
            else:
                assert my_shap[0].shape[0] == X.shape[1] + 1
                assert np.sum(np.abs(my_shap[0] - his_shap)) < 1e-10

    # Just check that this actually works
    instance = {str(f): np.float64(np.float32(v)) for f, v in enumerate(X[0, :])}

    sforest.predict(instance, explanation=True)


def test_iris():
    prediction_consistency("tests/data/iris.json.gz", True)


def test_diabetes():
    prediction_consistency("tests/data/diabetes.json.gz", True)


def test_yacht():
    prediction_consistency("tests/data/yacht.json.gz", False)


def test_iris_importance():
    X, y, fields = load_numeric_data("tests/data/iris.json.gz")
    predictor = sklearn_predictor(X, y, True)
    all_imps = shap_importances(predictor, fields, False)

    assert len(all_imps) == 3

    for imps in all_imps:
        assert len(imps) == 4
        assert all([len(imp) == 2 for imp in imps])
        assert abs(sum([imp[1] for imp in imps]) - 1.0) < 1e-8
        assert set([imps[0][0], imps[1][0]]) == set(["2", "3"]), imps


def test_yacht_importance():
    X, y, fields = load_numeric_data("tests/data/yacht.json.gz")
    predictor = sklearn_predictor(X, y, False)
    imps = shap_importances(predictor, fields, True)

    assert abs(sum([imp[1] for imp in imps]) - 1.0) < 1e-8
    assert imps[0][0] == "1", imps

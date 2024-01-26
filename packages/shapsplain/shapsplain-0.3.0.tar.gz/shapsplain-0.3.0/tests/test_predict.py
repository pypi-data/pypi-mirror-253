import random

import numpy as np

from bigml.anomaly import Anomaly

from bigml.bigmlconnection import HTTP_OK

from shapsplain.forest import ShapForest

from .utils import read_gzipped_json

SMALL_LC_ANOMALY = "tests/data/lending_club_anomaly.json.gz"


def anomaly_equivalence(modelfile, data, check_score=True):
    model = read_gzipped_json(modelfile)

    bml_detector = Anomaly({"object": model,
                            "resource": model["resource"],
                            "error": None,
                            "code": HTTP_OK})
    shap_forest = ShapForest(model)

    for i, d in enumerate(data):
        shap_score = shap_forest.predict(d)[0]
        bml_score = bml_detector.anomaly_score(d)

        assert abs(shap_score - bml_score) < 1e-5, str(i)

        if check_score and "remote_score" in data:
            assert abs(shap_score - data["remote_score"]) < 1e-5, str(i)

        if i % 16 == 0:
            shap_values = shap_forest.compute_shap(d)
            assert np.abs(shap_score - np.power(2, -np.sum(shap_values))) < 1e-8
            assert 0.35 < np.power(2, -shap_values[0][-1]) < 0.6


def test_in_sample():
    data = read_gzipped_json("tests/data/lc_tiny_scored.json.gz")
    anomaly_equivalence(SMALL_LC_ANOMALY, data)


def test_out_of_sample():
    data = read_gzipped_json("tests/data/lc_tiny_oss_scored.json.gz")
    anomaly_equivalence(SMALL_LC_ANOMALY, data)


def test_missing():
    data = read_gzipped_json("tests/data/lc_tiny_oss_scored.json.gz")
    rng = random.Random(0)

    for d in data:
        for key in d:
            if rng.random() > 0.5:
                d[key] = None

    anomaly_equivalence(SMALL_LC_ANOMALY, data, check_score=False)


def test_iris_explanation():
    data = read_gzipped_json("tests/data/iris.json.gz")
    model = read_gzipped_json("tests/data/iris_anomaly.json.gz")
    shap_forest = ShapForest(model)

    fnames = data[0]

    for d in data[1:8]:
        pt = {k: v for k, v in zip(fnames, d)}
        pt["sepal width"] = None

        exp = shap_forest.predict(pt, explanation=True)
        pred = shap_forest.predict(pt)

        assert np.abs(exp[0][0] - pred[0]) < 1e-8, (exp[0][0], pred[0])
        assert exp[0][1][0] == "000003"
        assert exp[0][1][1] > 0.1

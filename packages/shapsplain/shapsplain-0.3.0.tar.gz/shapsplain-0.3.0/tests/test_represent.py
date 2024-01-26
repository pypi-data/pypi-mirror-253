import shapsplain.importers

np = shapsplain.importers.import_numpy()

from shapsplain.represent import representatives


def sanity_checks(reps, original, npoints):
    repX = reps[:, :-1]
    repy = reps[:, -1]

    assert len(repX.shape) == 2
    assert repX.shape[0] == npoints, repX.shape
    assert repX.shape[1] == original.shape[1]
    assert repX.shape[0] <= original.shape[0]

    return repX, repy


def test_classify():
    npoints = 127
    X = np.random.random((1024, 5))
    y = np.zeros((1024, 4), dtype=np.float32)

    y[0:256, 0] = 1
    y[256:512, 1] = 1
    y[512:768, 2] = 1
    y[768:1024, 3] = 1

    Xy = representatives(X, y, npoints, True, 0)
    repX, repy = sanity_checks(Xy, X, npoints)

    for i in range(4):
        assert 24 < np.sum(repy == i) < 40, np.sum(repy == i)


def test_regression():
    for npoints in range(129, 137):
        X = np.ones((npoints + 2, 3))
        y = np.arange(npoints + 2, dtype=np.float32).reshape(-1, 1)

        Xy = representatives(X * y, y, npoints, True, npoints)
        repX, repy = sanity_checks(Xy, X, npoints)

        for row, cls in zip(repX, repy):
            assert np.all(row == cls), str((row, cls))

        yset = set(repy.tolist())
        assert len(yset) == npoints


def test_imbalanced():
    npoints = 127
    X = np.random.random((1024, 5))
    y = np.zeros((1024, 3), dtype=np.float32)

    y[0:900, 0] = 1
    y[900:1010, 1] = 1
    y[1010:1024, 2] = 1

    for i in range(8):
        Xy = representatives(X, y, npoints, False, i)
        repX, repy = sanity_checks(Xy, X, npoints)

        assert 70 < np.sum(repy == 0) < 90, np.sum(repy == 0)
        assert 20 < np.sum(repy == 1) < 40, np.sum(repy == 1)
        assert 14 == np.sum(repy == 2), np.sum(repy == 2)


def test_one_column():
    for npoints in range(129, 137):
        X = np.ones((npoints + 2, 1))
        y = np.arange(npoints + 2, dtype=np.float32).reshape(-1, 1)

        Xy = representatives(X * y, y, npoints, True, npoints)
        repX, repy = sanity_checks(Xy, X, npoints)

        for row, cls in zip(repX, repy):
            assert np.all(row == cls), str((row, cls))

        yset = set(repy.tolist())
        assert len(yset) == npoints


def test_short():
    npoints = 256
    X = np.random.random((npoints, 5))
    y = np.zeros((npoints, 4), dtype=np.float32)

    Xy = representatives(X, y, npoints, True, 0)
    repX, repy = sanity_checks(Xy, X, npoints)


def test_many_classes():
    npoints = 127
    X = np.random.random((1024, 5))
    y = np.random.random((1024, 32))

    Xy = representatives(X, y, npoints, True, 0)
    repX, repy = sanity_checks(Xy, X, npoints)


def test_stress():
    npoints = 1024
    X = np.random.random((4096, 2048))
    y = np.random.random((4096, 16))

    Xy = representatives(X, y, npoints, True, 0)
    repX, repy = sanity_checks(Xy, X, npoints)

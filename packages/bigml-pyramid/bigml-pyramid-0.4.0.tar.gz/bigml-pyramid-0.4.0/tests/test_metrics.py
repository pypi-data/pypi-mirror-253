import pyramid.importers

np = pyramid.importers.import_numpy()

from pyramid.train.metrics import classification_metrics


def test_usual_classification():
    y_true = np.array([[1, 0], [1, 0], [0, 1], [0, 1], [0, 1]])

    y_perfect = np.array(
        [[0.7, 0.3], [0.6, 0.4], [0.5, 0.5], [0.4, 0.6], [0.1, 0.9]]
    )

    perfect_mets = classification_metrics(y_true, y_perfect)

    for key in ["max_phi", "auc", "ndcg"]:
        assert perfect_mets[key] == 1.0, str((key, perfect_mets[key]))

    assert perfect_mets["accuracy"] == 0.8  # Ties are errors
    assert 0.5 < perfect_mets["likelihood"] < 1

    lousy_mets = classification_metrics(y_true, y_perfect[::-1])

    assert lousy_mets["accuracy"] == 0
    assert lousy_mets["auc"] == 0
    assert lousy_mets["max_phi"] < 0
    assert lousy_mets["likelihood"] < 0.3
    assert lousy_mets["ndcg"] < 0.6

    y_imperfect = np.array(
        [[0.7, 0.3], [0.6, 0.4], [0.8, 0.2], [0.4, 0.6], [0.1, 0.9]]
    )

    ok_mets = classification_metrics(y_true, y_imperfect)

    assert ok_mets["likelihood"] > 0.5
    assert ok_mets["accuracy"] == 0.8
    assert ok_mets["ndcg"] > 0.7
    assert 0.66 < ok_mets["auc"] < 0.67
    assert 0.66 < ok_mets["max_phi"] < 0.67


def test_strange():
    y_t1 = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
    y_t2 = np.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]])
    y_score = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])

    mets = classification_metrics(y_t1, y_score)
    assert mets["accuracy"] == 1.0
    assert mets["max_phi"] == 0.0  # it's undefined for uniform classes

    bad_mets = classification_metrics(y_t2, y_score)
    assert bad_mets["likelihood"] < 2e-15

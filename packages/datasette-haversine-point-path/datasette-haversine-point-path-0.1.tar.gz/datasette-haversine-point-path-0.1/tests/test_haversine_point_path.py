from datasette_haversine_point_path import prepare_connection
import sqlite3
import pytest

KD0FNR = 37.72489522009443, -122.422936174405
BELG = 51.9561076, 5.2400448
IONO = 45.07, -83.56
GAKONA = 62.38, -145
PTARGUELLO = 34.8,-120.5
SOPRON = 47.63,16.72

@pytest.fixture
def conn():
    conn = sqlite3.connect(":memory:")
    prepare_connection(conn)
    return conn


@pytest.mark.parametrize(
    "unit,expected",
    (
        ("ft", 5805047),
        ("m", 1769378.36),
        ("in", 69660567),
        ("mi", 1099.44),
        ("nmi", 955.39),
        ("km", 1769.38),
    ),
)
@pytest.mark.parametrize("type", (float, str))
def test_haversine_point_path(conn, unit, expected, type):
    actual = conn.execute(
        "select haversine_point_path(?, ?, ?, ?, ?, ?, ?)",
        [type(KD0FNR[0]), type(KD0FNR[1]), type(BELG[0]), type(BELG[1]), type(IONO[0]), type(IONO[1]), unit],
    ).fetchall()[0][0]
    assert expected == pytest.approx(actual, rel=1e-2)

@pytest.mark.parametrize(
    "unit,expected",
    (
        ("ft", 1206272),
        ("m", 367671.66),
        ("in", 14475263),
        ("mi", 228.7148841),
        ("nmi", 198.53),
        ("km", 367.67),
    ),
)
@pytest.mark.parametrize("type", (float, str))
def test_hav_not_perp(conn, unit, expected, type):
    actual = conn.execute(
        "select haversine_point_path(?, ?, ?, ?, ?, ?, ?)",
        [type(KD0FNR[0]), type(KD0FNR[1]), type(BELG[0]), type(BELG[1]), type(PTARGUELLO[0]), type(PTARGUELLO[1]), unit],
    ).fetchall()[0][0]
    assert expected == pytest.approx(actual, rel=1e-2)

@pytest.mark.parametrize(
    "unit,expected",
    (
        ("ft", 3132724),
        ("m", 954854.14),
        ("in", 37592684),
        ("mi", 593.32),
        ("nmi", 515.58),
        ("km", 954.85),
    ),
)
@pytest.mark.parametrize("type", (float, str))
def test_hav_not_perp_rx(conn, unit, expected, type):
    actual = conn.execute(
        "select haversine_point_path(?, ?, ?, ?, ?, ?, ?)",
        [type(KD0FNR[0]), type(KD0FNR[1]), type(BELG[0]), type(BELG[1]), type(SOPRON[0]), type(SOPRON[1]), unit],
    ).fetchall()[0][0]
    assert expected == pytest.approx(actual, rel=1e-2)

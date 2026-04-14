import pytest
from converter.length import (
    cm_to_m, m_to_cm, cm_to_inch, inch_to_cm,
    cm_to_km, km_to_cm, cm_to_feet, feet_to_cm,
    km_to_mile, mile_to_km
)

def test_cm_to_m():
    assert cm_to_m(100) == pytest.approx(1.0)

def test_m_to_cm():
    assert m_to_cm(1) == pytest.approx(100.0)

def test_cm_to_km():
    assert cm_to_km(100000) == pytest.approx(1.0)

def test_km_to_cm():
    assert km_to_cm(1) == pytest.approx(100000.0)

def test_cm_to_inch():
    assert cm_to_inch(2.54) == pytest.approx(1.0)

def test_inch_to_cm():
    assert inch_to_cm(1) == pytest.approx(2.54)

def test_cm_to_feet():
    assert cm_to_feet(30.48) == pytest.approx(1.0)

def test_feet_to_cm():
    assert feet_to_cm(1) == pytest.approx(30.48)

def test_km_to_mile():
    assert km_to_mile(1.609) == pytest.approx(1.0, rel=1e-3)

def test_mile_to_km():
    assert mile_to_km(1) == pytest.approx(1.609, rel=1e-3)

def test_zero_zawsze_daje_zero():
    assert cm_to_m(0) == pytest.approx(0.0)
    assert km_to_mile(0) == pytest.approx(0.0)

@pytest.mark.parametrize("cm, m", [
    (0,    0.0),
    (100,  1.0),
    (250,  2.5),
    (1000, 10.0),
])
def test_cm_to_m_parametrized(cm, m):
    assert cm_to_m(cm) == pytest.approx(m)

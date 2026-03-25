import pytest
from converter.mass import (
    g_to_kg, kg_to_g, kg_to_t, t_to_kg,
    mg_to_kg, kg_to_mg, mg_to_g, g_to_mg,
    kg_to_lb, lb_to_kg
)

def test_g_to_kg():
    assert g_to_kg(1000) == pytest.approx(1.0)

def test_kg_to_g():
    assert kg_to_g(1) == pytest.approx(1000.0)

def test_kg_to_t():
    assert kg_to_t(1000) == pytest.approx(1.0)

def test_kg_to_lb():
    assert kg_to_lb(1) == pytest.approx(2.20462)

def test_lb_to_kg():
    assert lb_to_kg(2.20462) == pytest.approx(1.0)

def test_odwrotnosc_kg_lb():
    # konwersja tam i z powrotem powinna dać oryginał
    assert lb_to_kg(kg_to_lb(5)) == pytest.approx(5.0)

def test_zero():
    assert g_to_kg(0) == pytest.approx(0.0)
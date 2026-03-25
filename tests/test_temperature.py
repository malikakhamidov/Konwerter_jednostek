import pytest
from converter.temperature import c_to_f, c_to_k, f_to_c, f_to_k, k_to_c, k_to_f

# --- podstawowe przypadki ---
def test_c_to_f_wrzenie():
    assert c_to_f(100) == pytest.approx(212.0)

def test_c_to_f_zamarzanie():
    assert c_to_f(0) == pytest.approx(32.0)

def test_c_to_k_zero():
    assert c_to_k(0) == pytest.approx(273.15)

def test_f_to_c_zamarzanie():
    assert f_to_c(32) == pytest.approx(0.0)

def test_f_to_c_wrzenie():
    assert f_to_c(212) == pytest.approx(100.0)

def test_k_to_c_zero_kelvin():
    assert k_to_c(273.15) == pytest.approx(0.0)

def test_k_to_f():
    assert k_to_f(373.15) == pytest.approx(212.0)

# --- edge case'y ---
def test_c_to_f_punkt_wspolny():
    # -40 to jedyna temperatura gdzie C == F
    assert c_to_f(-40) == pytest.approx(-40.0)

def test_f_to_k():
    assert f_to_k(32) == pytest.approx(273.15)

# --- parametryzacja: wiele wartości naraz ---
@pytest.mark.parametrize("celsius, fahrenheit", [
    (0,    32.0),
    (100,  212.0),
    (-40, -40.0),
    (37,   98.6),
])
def test_c_to_f_parametrized(celsius, fahrenheit):
    assert c_to_f(celsius) == pytest.approx(fahrenheit, rel=1e-3)
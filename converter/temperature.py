# Celsius to Fahrenheit
def c_to_f(v):
    return (v * 9/5) + 32


# Celsius to Kelvin
def c_to_k(v):
    return v + 273.15


# Fahrenheit to Celsius
def f_to_c(v):
    return (v - 32) * 5/9


# Fahrenheit to Kelvin
def f_to_k(v):
    return (v - 32) * 5/9 + 273.15


# Kelvin to Celsius
def k_to_c(v):
    return v - 273.15


# Kelvin to Fahrenheit
def k_to_f(v):
    return (v - 273.15) * 9/5 + 32

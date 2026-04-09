import pytest

def add(a,b):
    return a + b    

def test_add():
    assert add(4,5) == 9
    assert add(-1,1) == 0
    assert add(0,0) == 0    

def test_truth():
    assert True 

def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_subtract():
    assert 5 - 3 == 2
    assert 0 - 0 == 0
    assert -1 - 1 == -2

def test_multiply():
    assert 4 * 5 == 20
    assert -1 * 1 == -1
    assert 0 * 100 == 0

def test_divide():
    assert 10 / 2 == 5
    assert -9 / 3 == -3
    assert 0 / 1 == 0
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_modulus():
    assert 10 % 3 == 1
    assert 9 % 3 == 0
    assert -7 % 4 == 1

def test_exponentiation():
    assert 2 ** 3 == 8
    assert 5 ** 0 == 1
    assert (-2) ** 2 == 4

def test_floor_division():
    assert 10 // 3 == 3
    assert 9 // 2 == 4
    assert -7 // 4 == -2

def test_combined_operations():
    assert (2 + 3) * 4 == 20
    assert (10 - 2) / 4 == 2
    assert (3 ** 2) + (4 ** 2) == 25

def test_negative_numbers():
    assert -5 + -3 == -8
    assert -4 * -2 == 8
    assert -10 / 2 == -5

def test_zero_operations():
    assert 0 + 5 == 5
    assert 0 * 100 == 0
    assert 0 - 0 == 0

def test_large_numbers():
    assert 10**10 + 10**10 == 2 * 10**10
    assert 10**6 * 10**6 == 10**12
    assert 10**15 / 10**5 == 10**10

def test_float_operations():
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 1.5 * 2.0 == pytest.approx(3.0)
    assert 5.5 / 2.0 == pytest.approx(2.75)

def test_integer_division():
    assert 7 // 2 == 3
    assert -7 // 2 == -4
    assert 7 // -2 == -4

def test_modulus_negative():
    assert 7 % -3 == -2
    assert -7 % 3 == 2
    assert -7 % -3 == -1

def test_exponentiation_negative():
    assert 2 ** -3 == 0.125
    assert (-2) ** -2 == 0.25
    assert 5 ** -1 == 0.2

def test_add_param(a, b, result):
    assert add(a, b) == result
@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_param(a, b, result):
    assert add(a, b) == result      

def test_edge_cases():
    assert add(1e10, 1e10) == 2e10
    assert add(-1e10, 1e10) == 0
    assert add(1e-10, 1e-10) == 2e-10

def test_type_errors():
    with pytest.raises(TypeError):
        add("a", 1)
    with pytest.raises(TypeError):
        add(None, 5)
    with pytest.raises(TypeError):
        add([], {})

def test_commutative_property():
    assert add(3, 5) == add(5, 3)
    assert add(-1, 4) == add(4, -1)
    assert add(0, 0) == add(0, 0)

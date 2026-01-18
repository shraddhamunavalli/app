 from app import square

def test_square():
    result = square(5)
    print("Square of 5 =", result)
    assert result == 25

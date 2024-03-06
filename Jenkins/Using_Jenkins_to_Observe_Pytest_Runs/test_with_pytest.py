import random

def test_check_multiplication():
    a = random.randint(1, 2)
    b = random.randint(1, 2)
    c = random.randint(1, 4)

    assert a * b == c
        
test_check_multiplication()

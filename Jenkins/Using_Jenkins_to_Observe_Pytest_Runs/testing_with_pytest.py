# Script below has some errors, will be reviewed and corrected

import pytest
import random

def test_multiply_two_numbers(a, b, c):
    expression = a * b
    assert expression == c
    
a = random.randint(0, 3)
b = random.randint(0, 3)
c = random.randint(0, 9)
    
test_multiply_two_numbers(a, b, c)

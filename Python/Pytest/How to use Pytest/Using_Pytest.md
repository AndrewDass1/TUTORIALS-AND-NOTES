# How to use Pytest

1. Install Pytest:
```
pip install pytest
```
2. Specify importing pytest:
```
import pytest
```
3. Create functions that begins with "test_" and include assert statements
```
import pytest

def test_function1():
    calc2 = 2 + 3
    assert calc2 == 4

def test_function2():
    calc3 = 3 + 4
    assert calc3 == 5
```
4. Run the file by:
```
pytest (options) name_of_file.py
```
Using "options" is not required with pytest, but gives additional information. For further documentation how to run files with "options" can be found on the pytest official documentation: https://docs.pytest.org/en/6.2.x/usage.html <br>
<br>
Running this script will show there are two errors, since pytest reads the assert statements

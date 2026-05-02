import pytest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Bo'linmaning qiymati 0 ga teng bo'lishi mumkin emas.")
    return a / b

@pytest.fixture(params=[add, subtract, multiply, divide])
def operation(request):
    return request.param

def test_operation(operation):
    assert operation(5, 3) == 8
    assert operation(10, 4) == 6
    assert operation(7, 2) == 14
    assert operation(20, 5) == 4.0
```

```python
# test_operation.py
import pytest

def test_operation_add():
    assert add(5, 3) == 8

def test_operation_subtract():
    assert subtract(10, 4) == 6

def test_operation_multiply():
    assert multiply(7, 2) == 14

def test_operation_divide():
    assert divide(20, 5) == 4.0

def test_operation_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

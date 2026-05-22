from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def average(self, numbers: List[float]) -> float:
        return 50


def test_calculate_integration():
    mock_request = MockRequest({"numbers": [10, 4, 4, 2]})
    driver_handler = NumpyHandler()
    calculate4 = Calculator4(driver_handler)

    response = calculate4.calculate(mock_request)
    assert isinstance(response, dict)


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 1]})
    driver_handler = NumpyHandler()
    calculator4 = Calculator4(driver_handler)

    response = calculator4.calculate(mock_request)
    assert response == {'data': {'Calculator': 4, 'value': 1.0, 'Success': True}}


def test_calculate_integration_with_error():
    mock_request = MockRequest(body={"Something": 1})
    driver_handler = NumpyHandler()
    calculate4 = Calculator4(driver_handler)

    with raises(Exception) as execinfo:
        calculate4.calculate(mock_request)

    assert str(execinfo.value) == "body mal formatado"

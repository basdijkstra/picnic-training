import pytest

from pytest.examples.pytest_examples import Car


@pytest.fixture
def banana():
    car = Car('Ford', 'Focus', 'blue', 2022)
    yield car
    print(car.get_car_info())

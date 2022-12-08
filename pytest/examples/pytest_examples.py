import pytest


class Car:

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = self.check_year(year)

    def get_car_info(self):
        return f'This is a {self.year} {self.make} {self.model}'

    @staticmethod
    def check_year(year):
        if year < 1850:
            raise ValueError(f'The steam engine was not invented yet in {year}')
        return year

def test_car_info():
    my_car = Car('Ford', 'Focus', 2019)
    assert my_car.get_car_info() == 'This is a 2019 Ford Focus'


def test_incorrect_year_value_raises_error():
    with pytest.raises(ValueError) as ve:
        my_car = Car('Ford', 'WayTooOld', 1800)
    assert str(ve.value) == 'The steam engine was not invented yet in 1800'

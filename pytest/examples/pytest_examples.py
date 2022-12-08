import pytest


class Car:

    def __init__(self, make: str, model: str, color: str, year: int):
        self.make = make
        self.model = model
        self.color = color
        self.year = self.check_year(year)

    def get_car_info(self):
        return f'This is a {self.color} {self.year} {self.make} {self.model}'

    def is_a_recent_car(self):
        return self.year > 2015

    @staticmethod
    def check_year(year):
        if year < 1850:
            raise ValueError(f'The steam engine was not invented yet in {year}')
        return year

def test_car_info():
    my_car = Car('Ford', 'Focus', 'blue', 2019)
    assert my_car.get_car_info() == 'This is a blue 2019 Ford Focus'


def test_incorrect_year_value_raises_error():
    with pytest.raises(ValueError) as ve:
        my_car = Car('Ford', 'WayTooOld', 'black', 1800)
    assert str(ve.value) == 'The steam engine was not invented yet in 1800'


test_data = [
    ("Lamborghini", "Countach", 1988, False),
    ("Maserati", "Ghibli", 2016, True),
    ("Ford", "Focus", 2015, False),
]


@pytest.mark.parametrize("make, model, year, is_recent", test_data)
def test_is_car_recent(make, model, year, is_recent):
    my_car = Car(make, model, 'red', year)
    assert my_car.is_a_recent_car() == is_recent


# def test_is_my_lamborghini_recent():
#     my_car = car.Car("Lamborghini", "Countach", 1988)
#     assert my_car.is_a_recent_car() is False
#
#
# def test_is_my_maserati_recent():
#     my_car = car.Car("Maserati", "Ghibli", 2018)
#     assert my_car.is_a_recent_car() is True
#
#
# def test_is_my_ford_recent():
#     my_car = car.Car("Ford", "Focus", 2015)
#     assert my_car.is_a_recent_car() is True

@pytest.fixture
def car():
    car = Car('Ford', 'Focus', 'blue', 2022)
    yield car
    print(car.get_car_info())


def test_car_paint_job(car):
    car.color = 'red'

import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.cars import Car


def exp_create_car(session: orm.Session):
    car = Car()
    car.model = "Toyota"
    car.year = 2020
    session.add(car)
    session.commit()


def exp_get_all_cars(session: orm.Session):
    cars = session.query(Car).all()
    for car in cars:
        print(car.id, car.model, car.year)

def exp_get_toyota_2020(session: orm.Session):
    cars = session.query(Car).filter(Car.model == "Toyota", Car.year == 2020)
    for car in cars:
        print(car.id, car.model, car.year)

def exp_get_first_toyota_2020(session: orm.Session):
    car = session.query(Car).filter(Car.model == "Toyota", Car.year == 2020).first()
    print(car.id, car.model, car.year)

experiments = [
    exp_create_car,
    exp_get_all_cars,
    exp_get_toyota_2020,
    exp_get_first_toyota_2020
]

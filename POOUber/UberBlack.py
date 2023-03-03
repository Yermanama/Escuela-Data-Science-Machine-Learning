from car import Car

class UberBlack(Car):
    type_car_accepted = []
    seats_material = []

    def __init__(self, license, driver, type_car_accepted, seats_material):
        super().__init__(license, driver)
        UberBlack.type_car_accepted = type_car_accepted
        UberBlack.seats_material = seats_material

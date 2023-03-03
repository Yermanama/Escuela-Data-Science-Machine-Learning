from car import Car

class UberVan(Car):
    type_car_accepted = []
    seats_materials = []

    def __init__(self, license, driver, type_car_accepted, seats_materials):
        super().__init__(license, driver)
        UberVan.type_car_accepted = type_car_accepted
        UberVan.seats_materials = seats_materials

    def set_passenger(self, passenger_numero):
        if passenger_numero >= 6:
            self.__passenger = passenger_numero
            print(f"Pasajeros asignados: {str(self.__passenger)}")
        else:
            print("El número de pasajeros es demasiado bajo para entrar en esta categoría")
class Car ():
    id = int
    license = str
    driver = str
    passenger = int

    def __init__(self, license, driver):
        self.license = license
        self.driver = driver
    def set_passenger(self, passenger_numero):
        if passenger_numero >= 4:
            self.__passenger = passenger_numero
            print(f"Pasajeros asignados: {str(self.__passenger)}")
        else:
            print("El número de pasajeros es demasiado bajo para entrar en esta categoría")
    def get_passenger(self):
        if self.__passenger != int:
            print(self.__passenger)
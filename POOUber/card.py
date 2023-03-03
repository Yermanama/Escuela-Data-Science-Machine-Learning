from payment import Payment

class Card(Payment):
    nombre_titular = str
    numero_tarjeta = int
    CVV = int
    
    def __init__(self, nombre_titular, numero_tarjeta, CVV):
        super().__init__()
        self.nombre_titular = nombre_titular
        self.numero_tarjeta = numero_tarjeta
        self.CVV = CVV

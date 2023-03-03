from car import Car
from account import Account
from driver import Driver
from UberX import UberX
from UberVan import UberVan

if __name__ == "__main__":
    mi_uber = UberVan("123QWE", Driver("Germán Martínez", "445ZXC"), "Seat", "León")
    mi_uber.set_passenger(6)



from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, wheel_size, wheel_number, brand="", model=""):
        super().__init__(wheel_size, wheel_number)
        self.brand = brand
        self.model = model

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

    def honk(self):
        return "Beep beep!"
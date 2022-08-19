class Car:
    def __init__(self, company, model, color, speedLimit):
        self.company = company
        self.model = model
        self.color = color
        self.speedLimit = speedLimit

    def started(self):
        print("Car has started")

    def stoped(self):
        print("Car has stopped")

    def changingGear(self):
        print("Gear has been changed")

car1 = Car("Volkswagen", "Vento", "Blue", "240")
print(car1.company)
class Car:
    def __init__(self, color):
        self.engine_on = False
        self.color = color


    def start_engine(self):
        self.engine_on = True


    def drive_to(self, city):
        if self.engine_on:
            print(f'{self.color} едет в {city}')
        else:
            print('Машина не заведена')


car1 = Car('red')
car1.start_engine()
car1.drive_to('Dubna')
car2 = Car('blue')
car2.start_engine()
car2.drive_to('Moskow')
class Car:
    def __init__(self, model,color):
        self.model = model
        self.color = color



    def start_engine(self):
            return "Двигатель запущен."

    def stop_engine(self):
            return "Двигатель остановлен."

    car_count = 0
    def go(self):
        Car.car_count += 1
        return self.go

        #"задана скорость машины"

    def get_position (self,time):
        self.time *= self.go
        self.get_position = self.time

        return self.get_position
        #"Текущая позиция машины"


car_1 = Car("Kia", "black")
drive:50
print(repr(car_1))
# print(car_
# 1.output())
print(car_1.start_engine())
print(car_1.go(100))
print(car_1.get_position(50))

print(car_1.stop_engine())







class Car:

    def __init__(self, marka, year, color, consumption, tank_volume, mileage=0):
        self.marka = marka
        self.year = year
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен."

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."

    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return self.mileage

    def get_reserve(self):
        return self.reserve

    def __repr__(self):
        return f"Car({self.color}, {self.year}, {self.marka})"


##    def __str__(self):
##        return f"{self.color}, {self.year}, {self.marka})"
##        return "Car class Object"

# Simple method
##    def output(self):
##        #Car.car_count += 1
##        return f"{self.color}, {self.year}, {self.marka}"

car_1 = Car("Kia", 2020, "black", 10, 55)
print(repr(car_1))
print(car_1.color)
print(str(car_1.year))
# print(car_1.output())
print(car_1.start_engine())
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(300))
print(f"Пробег {car_1.get_mileage()} км.")
print(f"Запас топлива {car_1.get_reserve()} л.")
print(car_1.stop_engine())
print(car_1.drive(100))

##Вывод программы:
##Двигатель запущен.
##Проехали 100 км. Остаток топлива: 45.0 л.
##Проехали 100 км. Остаток топлива: 35.0 л.
##Проехали 100 км. Остаток топлива: 25.0 л.
##Малый запас топлива.
##Пробег 300 км.
##Запас топлива 25.0 л.
##Двигатель остановлен.
##Двигатель не запущен.
##

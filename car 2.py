class Car:
    def __init__(self, color, avefuelconsumption, fueltankvolume, fuelreserve, totalmileage):
        self.color = color
        self.avefuelconsumption = avefuelconsumption
        self.fueltankvolume = fueltankvolume
        self.fuelreserve = fuelreserve
        self.totalmileage = totalmileage

    def start_engine(self):
        if not self.engine_on and self.fuelreserve > 0:
            self.engine_on = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен."

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."


    def drive(self, distance):
        if self.engine_on:
            return "Двигатель не запущен."
        if self.fuelreserve / self.avefuelconsumption * 100 < distance:
            return "Малый запас топлива."
        self.totalmileage += distance
        self.fuelreserve -= distance / 100 * self.avefuelconsumption
            return f"Проехали { distance } км. Остаток топлива: { self.fuelreserve } л."


car_1 = Car(color = "blue", avefuelconsumption = 10, fueltankvolume = 55, fuelreserve = 20, totalmileage = 200)
print(car_1.start_engine())
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(300))
print(f"Пробег {car_1.get_totalmileage()} км.")
print(f"Запас топлива {car_1.get_fuelreserve()} л.")
print(car_1.stop_engine())
print(car_1.drive(100))
print(car_1.color)
print(car_1.avefuelconsumption,"средний расход топлива")
print(car_1.fueltankvolume,"объем топливного бака")
print(car_1.fuelreserve,"запас топлива")
print(car_1.totalmileage,"общий пробег")

car_2 = Car(color = "green", avefuelconsumption = 13, fueltankvolume = 60, fuelreserve = 35, totalmileage = 15)
print(car_2.color)
print(car_2.avefuelconsumption,"средний расход топлива")
print(car_2.fueltankvolume,"объем топливного бака")
print(car_2.fuelreserve,"запас топлива")
print(car_2.totalmileage,"общий пробег")
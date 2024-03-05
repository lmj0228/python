from car import Car

my_new_car = Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23 # 속성이 public이다
my_new_car.read_odometer()
my_new_car.update_odometer(11)
my_new_car.read_odometer()
my_new_car.increment_odometer(23_500)
my_new_car.read_odometer()

class Battery:
    """배터리"""
    def __init__(self,battery_size=00):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"차량 배터리 크기는 {self.battery_size}")

    def get_range(self):
        if self.battery_size < 40:
            return(150)
        elif self.battery_size > 65:
            return(225)

class ElectricCar(Car):
    """전기차"""
    def __init__(self, make,model,year, large_battery=Battery()):
        super().__init__(make,model,year)
        self.battery = large_battery

    def describe_battery(self):
        return(f"이차 배터리 용량은 {self.battery.battery_size}")
    
    def get_descriptive_name(self):
        print(super().get_descriptive_name())
        print(f"차량 배터리 크기는 {self.battery.battery_size}")

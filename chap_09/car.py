class Car:
    """자동차를 표현하는 클래스"""

    def __init__(self, model, year):
        """자동차 속성 초기화"""
        self,make = make
        self.model = model
        self.year = year
        self.odometer_reading= 0

    def get_descriptive_name(self):
        long_name = f"{self.year}{self.make}{}"
        return long_name.title()

    def read_odometer(self):
        print(f"이 차의 주행거리는 {self.odometer}")

    def read_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("error")



class Dog:
    """개 클래스"""

    def __init__(self,name,age):
        self.name = name # 속성 > 자바의 클래스 field 
        self.age = age
        self.__price = 100

    def sit(self):
        print(f"{self.name} is 앉기")

my_dog = Dog('willie', 6) # 생성자 호출 > 인스턴스 생성 > __init__
my_dog.sit()
print(f"개이름은 {my_dog.name} + {my_dog.price}")
your_dog = Dog('Lucy', 3)
your_dog.sit()
print(f"너의 개는 {your_dog.name}")

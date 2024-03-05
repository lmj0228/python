class Person:
    count = 0 ### 클래스 변수 - 중요
    def __init__(self,name,age,address): #생성자 역할
        self.name=name ### 인스턴스 변수
        self.age=age
        self.address=address
        self.weight = [65,67,70,71] # 공개 속성
        self.height = 170 #private 속성

        print("{}객체가 생성됨".format(self.name))
        Person.count += 1 ### 클래스 변수를 증가

    @classmethod ### decorator - 자바 용어는 annotation
    def printing(cls):
        print("객체수는 {}".format(cls.count))
        
    def __getitem__(self, indx):
        return self.weight[indx]
    def __del__(self):
        print("객체 {}이 소멸됨".format(self.name))

Person('guest',11,'jeju')

new_person = Person('hong',20,'busan')
other_person = Person('kim',30,'busan')
Person.printing() ### 클래스 메서드 호출
new_person.printing()

print(f'person 객체의 나이는**{new_person.age:5}***')
print("객체의 타입은 {}".format(isinstance(new_person, Person)))
print(f"현재 체중은 {new_person[2]}")
print(f"{other_person.count} 객체가 생성됨")

class Restaurant:
    def __init__(self, rname, rtype):
        self.restaurant_name = rname
        self.cuisine_type = rtype

    def describe_restaurant(self):
        print()

    def open_restaurant(self):
        print()

class IceCreamStand(Restaurant):
    def __init__(self, name, ctype, flavors):
        super().__init__(name, ctype)
        self.flavors = flavors

    def show_flavors(self):
        print("맛이 {}".format(self.flavors))
        print(f"맛이 {self.flavors}")  
    
new_rest = Restaurant('백다방','cafe')
ice_cream = IceCreamStand('Italt','pizza','매운맛')
ice_cream.show_flavors()

print(f"레스토랑 이름과 타입 {new_rest.restaurant_name} {new_rest.cuisine_type}")
new_rest.describe_restaurant()

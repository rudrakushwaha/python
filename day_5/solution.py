class Car:

    def __init__(self, brand, model):
        self.__brand = brand          #making brand variable as private by adding __ at start
        self.model = model  

    def get_brand(self):
        return self.__brand 

    def name(self):
        #return f"{self.brand} {self.model}"
        print(f"car name:   {self.__brand}  {self.model} ")

class ElectricCar(Car):

    def __init__(self, brand , model , battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
  

   


myCar = Car("Audi" , "A8")          #creating object
# print(myCar.brand)
# print(myCar.model)
# myCar.name()                   

my_tesla = ElectricCar("Tesla" , "Model S", "85kWh")
# my_tesla.name()
#print(my_tesla.__brand)  # now we can't access the brand varibale directly as we made it private, therefore access it through getter
print(my_tesla.get_brand())










#setter is left

# [
#     ("1","audit","warn","2026"),
#     ("2","audit","error","2025"),
#     ("3","audit","error","2025"),
#     ("4","payment","warn","2026"),
#     ("5","payment","error","2026"),
#     ("6","payment","error","2026"),
#     ("7","payment","error","2026"),
#     ("8","sales","warn","2026")
# ]
# print the whole entries as per descending order of the error count

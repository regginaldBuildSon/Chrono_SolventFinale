##Functions in a class are methods
##Their variables are called attributes
class Fruit:
    def __init__(self, name, clr):
        self.name=  name
        self.color= clr
        
    def details(self):
        exp_date = "07.21.2023"
        print("my " + self.name + " is " + self.color)
        print("I expire on " + exp_date)
        
apple = Fruit("apple", "red")
apple.details()
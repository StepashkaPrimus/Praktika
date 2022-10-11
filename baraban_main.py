import random



class baraban:
    def __init__(self):
        self.values = [100,200,300]
        self.values_1 = ["X2", "X3"]

    def get_random_value(self):
        numbers = self.values[random.randint(0,2)]
        multiplication = self.values_1[random.randint(0,1)]
        print(numbers)
        print(multiplication)
        return numbers
numbers = baraban()
numbers.get_random_value()








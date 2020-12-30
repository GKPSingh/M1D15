class Math:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addition(self):
        return self.a + self.b + self.c

    def multiplication(self):
        return self.a * self.b * self.c

    def division(self):
        return (self.a * self.b) / self.c

    def subtraction(self):
        return (self.a * self.b) - self.c

    def calculate(self):
        print(self.addition())
        print(self.multiplication())
        print(self.division())
        print(self.subtraction())



if __name__ == "__main__":
    #obj1 = Math(4, 5, 2)
    #sum = obj1.addition()
    #print(sum)

    #product = obj1.multiplication()
    #print(product)

    obj2 = Math(7, 5, 2)
    #divide = obj2.division()
    #print(divide)


    obj2.calculate()
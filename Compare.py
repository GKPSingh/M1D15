class Comparison:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def smaller(self):
        if self.x < self.y:
            return self.x
        else:
            return self.y

    def larger(self):
        if self.x > self.y:
            return self.x
        else:
            return self.y

    def equal(self):
        if self.x == self.y:
            return 'Both numbers are equal'

    def compute(self):
        print(f'smaller number is {self.smaller()}')
        print(f'larger number is {self.larger()}')
        print(f'{self.equal()}')




if __name__ == "__main__":

    # obj1 = Comparison(7, 5)
    # small = obj1.smaller()
    # print(small)
    #
    #
    # obj2  = Comparison(3, 9)
    # large = obj2.larger()
    # print(large)
    #
    # obj3 = Comparison(5,5)
    # same = obj3.equal()
    # print(same)

    compare = Comparison(9, 9)
    compare.compute()










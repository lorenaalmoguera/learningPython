class Classy:
    def method(self, par):
        print("method:", par)
 
 
obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

class Classy2:
    varia = 2
    def method(self):
        print(self.varia, self.var)
 
 
obj = Classy2()
obj.var = 3
obj.method()

class Classy3:
    def __init__(self, value = None):
        self.var = value


obj_1 = Classy3("object")
obj_2 = Classy3()

print(obj_1.var)
print(obj_2.var)


class ClassyHidden:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = ClassyHidden()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._ClassyHidden__hidden()

class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')


    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
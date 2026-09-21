#Single Inheritance

class Grandfather:
    def house(self):
        print("Grandfather has a house")
class Father(Grandfather):
    def car(self):
        print("Father has a car")
f=Father()
f.house()
f.car()

#Multilevel Inheritance

class Grandfather:
    def house(self):
        print("Grandfather has a house")
class Father(Grandfather):
    def car(self):
        print("Father has a car")
class Son(Father):
    def bike(self):
        print("Son has a bike")
s=Son()
s.house()
s.car()
s.bike()

#Hierarchical Inheritance

class Father:
    def house(self):
        print("Father has a house")
class Son(Father):
    def bike(self):
        print("Son has a bike")
class Daughter(Father):
    def car(self):
        print("Daughter has a car")
s = Son()
s.house()
s.bike()
d = Daughter()
d.house()
d.car()

#Multiple Inheritance

class Father:
    def car(self):
        print("Father has a car")
class Mother:
    def food(self):
        print("Mother makes food")
class Son(Father, Mother):
    pass
s = Son()
s.car()
s.food()

#Hybrid Inheritance

class Grandfather:
    def house(self):
        print("Grandfather has a house")
class Father(Grandfather):
    def car(self):
        print("Father has a car")
class Son(Father):
    def bike(self):
        print("Son has a bike")
class Daughter(Father):
    def gold(self):
        print("Daughter has gold")
s = Son()
s.house()
s.car()
s.bike()

class A:
    def S(self):
        print("A")
class B:
    def S(self):
        print("B")

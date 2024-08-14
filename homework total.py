# 1
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
c1=person("ali", 22)
print(c1.name)
print(c1.age)
# 2
class greetting:
    def __init__(self, greeting):
        self.greeing='hello how are you'
h= greetting('ali')
print(h.greeing)
# 3
class car:
    def __init__(self, name, date, year, model):
        self.name= name
        self.date= date
        self.year= year
        self.model= model
    def __repr__(self):
        return (f"name=clora", "date=now day", "year=2012", "model=tyota")

dd= car("clora", "2012", "2012", "tyota")
print(dd.__repr__())
# 4
import math
class circle:
    def __init__(self, radius):
        self.darius= radius
    def earia(self, radius):
        self.darius=4
e= circle(math.pi*4**2)
print(e.darius)
# 6
# inhertince and polymorghisme
class animal:
    def __init__(self, name, sound):
        self.name= name
        self.sound=sound
    def dog(self, animal):
        self.mane='anme'
        self.sound='sound'
    def cat(self, animal):
        self.name= 'anme'
        self.sound='sound'

d=animal("dog", "bark")
print(d.name)
print(d.sound)
c=animal("cat", "Mewo")
print(c.name)
print(c.sound)
# 7
class math:
    def __init__(self, length, width):
        self.length= length
        self.width=width
class tringle:
    def __init__(self,radius,length, width):
        self.radius= radius

class square:
    def __init__(self,length, width):
     def earia1(square):
         return width*length
     def earia(tringle):
        return earia(width(length)/2)
s=square(2,3)
print(s)
t=tringle(2,4,6)
print(t)
# 8






# fron oop the 40 question
# 14    %%%%%% 14 %%%%%%%
class BankAccount:
    def __init__(self, account_number, initial_balance ):
        self.__account_numbre=account_number
        self.__balance=initial_balance
    def desposit(self, amount):
        self.__balance+=amount
    def withdraw(self , amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("indusaficient is fount ")
    def check_balance(self):
        return self.__balance
account=BankAccount("123456789", 1000)
account.desposit(500)
print(account.check_balance())
account.withdraw(200)
print(account.check_balance())

# 15 %%%%%%% 15 %%%%%%%%%%%
class student:
    def __init__(self, name, grade, age):
        self.name= name
        self.grade= grade
        self.age= age
    def get_name(self):
        return self .__name
    def __set_name__(self, name):
        self.__set_name= name

    # def get_grade(self):
    #     return self.__grade
    # def set_grade(slef, grade, self=None):
    #     return self.__grade=grade
    # def get_age(self):
    #     return self.__age
    # def set_age(self, age):
    #     self.__age=age
    # def display_details(self):
# print(f"Name:{self.name}, grade:{self.grade}, age:{self.__age}")
# 16
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Removed '{book_title}' from the library.")
                return
        print(f"Book '{book_title}' not found in the library.")

# Creating instances of Book and Library classes
book1 = Book("Python Programming", "John Doe")
book2 = Book("Data Structures", "Jane Smith")

library = Library("My Library")
library.add_book(book1)
library.add_book(book2)

library.remove_book("Python Programming")
library.remove_book("Art of War")

# Added 'Python Programming' by John Doe to the library.
# Added 'Data Structures' by Jane Smith to the library.
# Removed 'Python Programming' from the library.
# Book 'Art of War' not found in the library.
# %%%%%%%%%%%%%%%%% 17 %%%%%%%%%%%%
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"{student.name} has been added to {self.name}")
        else:
            print("Invalid student object")

    def remove_student(self, student_name):
        for s in self.students:
            if s.name == student_name:
                self.students.remove(s)
                print(f"{student_name} has been removed from {self.name}")
                return
        print(f"{student_name} not found in {self.name}")

# Example usage
s1 = Student("John", 15)
s2 = Student("Alice", 16)

school1 = School("ABC High School")
school1.add_student(s1)  # Output: John has been added to ABC High School
school1.add_student(s2)  # Output: Alice has been added to ABC High School

print([s.name for s in school1.students])  # Output: ['John', 'Alice']

school1.remove_student("John")  # Output: John has been removed from ABC High School

print([s.name for s in school1.students])  # Output: ['Alice']

# %%%%%%%%%%%%%%%%  18  %%%%%%%%%%%%%%

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        if isinstance(person, Person):
            self.members.append(person)
            print(f"{person.name} has been added to {self.name}")
        else:
            print("Invalid person object")

    def remove_member(self, person_name):
        for p in self.members:
            if p.name == person_name:
                self.members.remove(p)
                print(f"{person_name} has been removed from {self.name}")
                return
        print(f"{person_name} not found in {self.name}")

# Example usage
p1 = Person("John", 25)
p2 = Person("Alice", 30)

team1 = Team("Football Team")
team1.add_member(p1)  # Output: John has been added to Football Team
team1.add_member(p2)  # Output: Alice has been added to Football Team

print([p.name for p in team1.members])  # Output: ['John', 'Alice']

team1.remove_member("John")  # Output: John has been removed from Football Team

print([p.name for p in team1.members])  # Output: ['Alice']

# %%%%%%%%%%% 19 %%%%%%%%%%%%

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            print(f"{employee.name} has been added to {self.name}")
        else:
            print("Invalid employee object")

    def remove_employee(self, employee_name):
        for e in self.employees:
            if e.name == employee_name:
                self.employees.remove(e)
                print(f"{employee_name} has been removed from {self.name}")
                return
        print(f"{employee_name} not found in {self.name}")

# Example usage
e1 = Employee("John", 25, 50000)
e2 = Employee("Alice", 30, 60000)

company1 = Company("ABC Company")
company1.add_employee(e1)  # Output: John has been added to ABC Company
company1.add_employee(e2)  # Output: Alice has been added to ABC Company

print([e.name for e in company1.employees])  # Output: ['John', 'Alice']

company1.remove_employee("John")  # Output: John has been removed from ABC Company

print([e.name for e in company1.employees])  # Output: ['Alice']

# %%%%%%%%%%%%%% 20 %%%%%%%%%%
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.name} has been added to {self.name}")
        else:
            print("Invalid animal object")

    def remove_animal(self, animal_name):
        for a in self.animals:
            if a.name == animal_name:
                self.animals.remove(a)
                print(f"{animal_name} has been removed from {self.name}")
                return
        print(f"{animal_name} not found in {self.name}")

# Example usage
a1 = Animal("Lion", "Panthera leo")
a2 = Animal("Tiger", "Panthera tigris")

zoo1 = Zoo("ABC Zoo")
zoo1.add_animal(a1)  # Output: Lion has been added to ABC Zoo
zoo1.add_animal(a2)  # Output: Tiger has been added to ABC Zoo

print([a.name for a in zoo1.animals])  # Output: ['Lion', 'Tiger']

zoo1.remove_animal("Lion")  # Output: Lion has been removed from ABC Zoo

print([a.name for a in zoo1.animals])  # Output: ['Tiger']


# 22
import tkinter as tk
from tkinter import ttk
root=tk.Tk()
tk.Button(root, text='open', background='red').pack()
root.mainloop()
# 23
a=("s", "e", "w", "q", "t")
x=slice(3,5)
print(a[x])
# 24
a=(1,2,3,)
x=sorted(a)
print(x)
# 25
# class calculator:
#     def total(self, num1, num2):
#         return num1+num2
# calculator.total= staticmethod(calculator.total)
# sum= calculator.total(5,5)
# print("sum:", sum)

#26
n3=16
print(str(n3))

# 27
numbers= [1,2,3,4,5,6,7,8,0]
numbers_sum=sum(numbers)
print("the sum is :", sum)

# 28

class parent:
    def __init__(self, txt):
        self.massage=txt
    def printmassage(self):
        print(self.massage)

# 29
t=tuple([1,2,3,4,5,6,7,8])
print(t)
# 30
n= "ahmad"
print(type(n))
# 31

print(vars(int))

# 32
top= ['reza', 'anwer']
ver= [12,13,14]
result= zip(top, ver, )
print(list(result))
# 33
# np= __import__('numpy', globals(), locals(), [], 0)
# a= np.array([2,3,4])
print(type(a))

import tkinter as tk
from tkinter import ttk
root=tk.Tk()
button=tk.Button(root , text='open', background='red').pack()
root.mainloop()






# 52
print(dir(string))
# 53
print(divmod(2,44))
# 54
print(list(enumerate([1,2,3,3,4,5,6,7,8])))
# 55
x='point'
eval(x)
# 56
x= 'name'
exec(x)
# 57
list=[1,2,3,4,5,6]
x=(filter(list))
# 57
print(float(5))
# 58
format(23,'%')
# that code is worked is builtin function ok thank you from my teacher


# 1
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
c1=person("ali", 22)
print(c1.name)
print(c1.age)
# 2
class greetting:
    def __init__(self, greeting):
        self.greeing='hello how are you'
h= greetting('ali')
print(h.greeing)
# 3
class car:
    def __init__(self, name, date, year, model):
        self.name= name
        self.date= date
        self.year= year
        self.model= model
    def __repr__(self):
        return (f"name=clora", "date=now day", "year=2012", "model=tyota")

dd= car("clora", "2012", "2012", "tyota")
print(dd.__repr__())
# 4
import math
class circle:
    def __init__(self, radius):
        self.darius= radius
    def earia(self, radius):
        self.darius=4
e= circle(math.pi*4**2)
print(e.darius)
# 6
# inhertince and polymorghisme
class animal:
    def __init__(self, name, sound):
        self.name= name
        self.sound=sound
    def dog(self, animal):
        self.mane='anme'
        self.sound='sound'
    def cat(self, animal):
        self.name= 'anme'
        self.sound='sound'

d=animal("dog", "bark")
print(d.name)
print(d.sound)
c=animal("cat", "Mewo")
print(c.name)
print(c.sound)
# 7
class math:
    def __init__(self, length, width):
        self.length= length
        self.width=width
class tringle:
    def __init__(self,radius,length, width):
        self.radius= radius

class square:
    def __init__(self,length, width):
     def earia1(square):
         return width*length
     def earia(tringle):
        return earia(width(length)/2)
s=square(2,3)
print(s)
t=tringle(2,4,6)
print(t)
# 8






# fron oop the 40 question
# 14    %%%%%% 14 %%%%%%%
class BankAccount:
    def __init__(self, account_number, initial_balance ):
        self.__account_numbre=account_number
        self.__balance=initial_balance
    def desposit(self, amount):
        self.__balance+=amount
    def withdraw(self , amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("indusaficient is fount ")
    def check_balance(self):
        return self.__balance
account=BankAccount("123456789", 1000)
account.desposit(500)
print(account.check_balance())
account.withdraw(200)
print(account.check_balance())

# 15 %%%%%%% 15 %%%%%%%%%%%
class student:
    def __init__(self, name, grade, age):
        self.name= name
        self.grade= grade
        self.age= age
    def get_name(self):
        return self .__name
    def __set_name__(self, name):
        self.__set_name= name

    # def get_grade(self):
    #     return self.__grade
    # def set_grade(slef, grade, self=None):
    #     return self.__grade=grade
    # def get_age(self):
    #     return self.__age
    # def set_age(self, age):
    #     self.__age=age
    # def display_details(self):
# print(f"Name:{self.name}, grade:{self.grade}, age:{self.__age}")
# 16
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Removed '{book_title}' from the library.")
                return
        print(f"Book '{book_title}' not found in the library.")

# Creating instances of Book and Library classes
book1 = Book("Python Programming", "John Doe")
book2 = Book("Data Structures", "Jane Smith")

library = Library("My Library")
library.add_book(book1)
library.add_book(book2)

library.remove_book("Python Programming")
library.remove_book("Art of War")

# Added 'Python Programming' by John Doe to the library.
# Added 'Data Structures' by Jane Smith to the library.
# Removed 'Python Programming' from the library.
# Book 'Art of War' not found in the library.
# %%%%%%%%%%%%%%%%% 17 %%%%%%%%%%%%
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"{student.name} has been added to {self.name}")
        else:
            print("Invalid student object")

    def remove_student(self, student_name):
        for s in self.students:
            if s.name == student_name:
                self.students.remove(s)
                print(f"{student_name} has been removed from {self.name}")
                return
        print(f"{student_name} not found in {self.name}")

# Example usage
s1 = Student("John", 15)
s2 = Student("Alice", 16)

school1 = School("ABC High School")
school1.add_student(s1)  # Output: John has been added to ABC High School
school1.add_student(s2)  # Output: Alice has been added to ABC High School

print([s.name for s in school1.students])  # Output: ['John', 'Alice']

school1.remove_student("John")  # Output: John has been removed from ABC High School

print([s.name for s in school1.students])  # Output: ['Alice']

# %%%%%%%%%%%%%%%%  18  %%%%%%%%%%%%%%

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        if isinstance(person, Person):
            self.members.append(person)
            print(f"{person.name} has been added to {self.name}")
        else:
            print("Invalid person object")

    def remove_member(self, person_name):
        for p in self.members:
            if p.name == person_name:
                self.members.remove(p)
                print(f"{person_name} has been removed from {self.name}")
                return
        print(f"{person_name} not found in {self.name}")

# Example usage
p1 = Person("John", 25)
p2 = Person("Alice", 30)

team1 = Team("Football Team")
team1.add_member(p1)  # Output: John has been added to Football Team
team1.add_member(p2)  # Output: Alice has been added to Football Team

print([p.name for p in team1.members])  # Output: ['John', 'Alice']

team1.remove_member("John")  # Output: John has been removed from Football Team

print([p.name for p in team1.members])  # Output: ['Alice']

# %%%%%%%%%%% 19 %%%%%%%%%%%%

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            print(f"{employee.name} has been added to {self.name}")
        else:
            print("Invalid employee object")

    def remove_employee(self, employee_name):
        for e in self.employees:
            if e.name == employee_name:
                self.employees.remove(e)
                print(f"{employee_name} has been removed from {self.name}")
                return
        print(f"{employee_name} not found in {self.name}")

# Example usage
e1 = Employee("John", 25, 50000)
e2 = Employee("Alice", 30, 60000)

company1 = Company("ABC Company")
company1.add_employee(e1)  # Output: John has been added to ABC Company
company1.add_employee(e2)  # Output: Alice has been added to ABC Company

print([e.name for e in company1.employees])  # Output: ['John', 'Alice']

company1.remove_employee("John")  # Output: John has been removed from ABC Company

print([e.name for e in company1.employees])  # Output: ['Alice']

# %%%%%%%%%%%%%% 20 %%%%%%%%%%
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.name} has been added to {self.name}")
        else:
            print("Invalid animal object")

    def remove_animal(self, animal_name):
        for a in self.animals:
            if a.name == animal_name:
                self.animals.remove(a)
                print(f"{animal_name} has been removed from {self.name}")
                return
        print(f"{animal_name} not found in {self.name}")

# Example usage
a1 = Animal("Lion", "Panthera leo")
a2 = Animal("Tiger", "Panthera tigris")

zoo1 = Zoo("ABC Zoo")
zoo1.add_animal(a1)  # Output: Lion has been added to ABC Zoo
zoo1.add_animal(a2)  # Output: Tiger has been added to ABC Zoo

print([a.name for a in zoo1.animals])  # Output: ['Lion', 'Tiger']

zoo1.remove_animal("Lion")  # Output: Lion has been removed from ABC Zoo

print([a.name for a in zoo1.animals])  # Output: ['Tiger']


# 23
a=("s", "e", "w", "q", "t")
x=slice(3,5)
print(a[x])
# 24
a=(1,2,3,)
x=sorted(a)
print(x)
# 25
# class calculator:
#     def total(self, num1, num2):
#         return num1+num2
# calculator.total= staticmethod(calculator.total)
# sum= calculator.total(5,5)
# print("sum:", sum)

#26
n3=16
print(str(n3))

# 27
numbers= [1,2,3,4,5,6,7,8,0]
numbers_sum=sum(numbers)
print("the sum is :", sum)

# 28

class parent:
    def __init__(self, txt):
        self.massage=txt
    def printmassage(self):
        print(self.massage)

# 29
t=tuple([1,2,3,4,5,6,7,8])
print(t)
# 30
n= "ahmad"
print(type(n))
# 31

print(vars(int))

# 32
top= ['reza', 'anwer']
ver= [12,13,14]
result= zip(top, ver, )
print(list(result))
# 33
# np= __import__('numpy', globals(), locals(), [], 0)
# a= np.array([2,3,4])
print(type(a))


# 1
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
c1=person("ali", 22)
print(c1.name)
print(c1.age)
# 2
class greetting:
    def __init__(self, greeting):
        self.greeing='hello how are you'
h= greetting('ali')
print(h.greeing)
# 3
class car:
    def __init__(self, name, date, year, model):
        self.name= name
        self.date= date
        self.year= year
        self.model= model
    def __repr__(self):
        return (f"name=clora", "date=now day", "year=2012", "model=tyota")

dd= car("clora", "2012", "2012", "tyota")
print(dd.__repr__())
# 4
import math
class circle:
    def __init__(self, radius):
        self.darius= radius
    def earia(self, radius):
        self.darius=4
e= circle(math.pi*4**2)
print(e.darius)
# 6
# inhertince and polymorghisme
class animal:
    def __init__(self, name, sound):
        self.name= name
        self.sound=sound
    def dog(self, animal):
        self.mane='anme'
        self.sound='sound'
    def cat(self, animal):
        self.name= 'anme'
        self.sound='sound'

d=animal("dog", "bark")
print(d.name)
print(d.sound)
c=animal("cat", "Mewo")
print(c.name)
print(c.sound)
# 7
class math:
    def __init__(self, length, width):
        self.length= length
        self.width=width
class tringle:
    def __init__(self,radius,length, width):
        self.radius= radius

class square:
    def __init__(self,length, width):
     def earia1(square):
         return width*length
     def earia(tringle):
        return earia(width(length)/2)
s=square(2,3)
print(s)
t=tringle(2,4,6)
print(t)
# 8
class employee:
    def __init__(self, name, lname, age, salary):
        self.name = name
        self.lname = lname
        self.age = age
        self.salary = salary


class manager:
    def employee(manager):
        def __init__(self, departament):
            departament = 'IT'


e = employee("mohammad ", "ahmadi", 22, 2000)
print(e.name)
print(e.lname)
print(e.age)
print(e.salary)
print()


# 9
class wehicle:
    def __init__(self, name, whire, kind):
        self.name = name
        self.whire = whire
        self.kind = kind


class track(wehicle):
    def wehicle(self, fast):
        self.fast = fast


class bicke(wehicle):
    def bicke(self, slowly):
        self.slowly = slowly


q = track("track", "six whire", "car", )
print(q.name)
w = bicke("bick", "towhire", "bicke")
print(w.name)


# 10
class bird:
    def __init__(self, name, kind, fly, run):
        self.name = name
        self.kind = kind
        self.fly = fly
        self.run = run


class eagle(bird):
    def eagle(self, fly):
        self.fly = fly


class penguin(bird):
    def penguin(self, run):
        self.run = run


s = bird("eagle", "bird", "fly", 0)
print(s.name)
e = bird("penguin", "bird", 0, "running")
print(e.name)


# 11
# encubsolation and abstraction
class account:
    def __init__(self, n_b=0):
        self.__b = n_b

    def dep(self, amount):
        if amount > 0:
            self.__b += amount
            return True
        else:
            return False

    def withraw(self, amount):
        if 0 < amount <= self.__b:
            self.__b -= amount
            return True
        else:
            return False

    def get_b(self):
        return self.__b


cc = account(100)
print(cc.get_b())
cc.dep(50)
print(cc.get_b)
cc.withraw(30)
print(cc.get_b())
# 12
class book:
    def __init__(self, title ,author , page):
        self.__title=title
        self.__author=author
        self.__page= page
    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title= title
    def get_author(self):
        return self.__author
    def set_author(self, author):
        self._author= author

    def get_page(self):
        return self.__page

    def set_page(self, page):
        self._page =page

# 13
class laptop:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model= model
        self.price= price
    def apply_discount(self, discount_per):
        self.price= self.price-(self.price * (discount_per/100))
    def display_details(self):
        print(f"brand:{self.brand}")
        print(f"model:{self.model}")
        print(f"price:{self.price}")

# 14





# fron oop the 40 question
# 14    %%%%%% 14 %%%%%%%
class BankAccount:
    def __init__(self, account_number, initial_balance ):
        self.__account_numbre=account_number
        self.__balance=initial_balance
    def desposit(self, amount):
        self.__balance+=amount
    def withdraw(self , amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("indusaficient is fount ")
    def check_balance(self):
        return self.__balance
account=BankAccount("123456789", 1000)
account.desposit(500)
print(account.check_balance())
account.withdraw(200)
print(account.check_balance())

# 15 %%%%%%% 15 %%%%%%%%%%%
class student:
    def __init__(self, name, grade, age):
        self.name= name
        self.grade= grade
        self.age= age
    def get_name(self):
        return self .__name
    def __set_name__(self, name):
        self.__set_name= name

    # def get_grade(self):
    #     return self.__grade
    # def set_grade(slef, grade, self=None):
    #     return self.__grade=grade
    # def get_age(self):
    #     return self.__age
    # def set_age(self, age):
    #     self.__age=age
    # def display_details(self):
# print(f"Name:{self.name}, grade:{self.grade}, age:{self.__age}")
# 16
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Removed '{book_title}' from the library.")
                return
        print(f"Book '{book_title}' not found in the library.")

# Creating instances of Book and Library classes
book1 = Book("Python Programming", "John Doe")
book2 = Book("Data Structures", "Jane Smith")

library = Library("My Library")
library.add_book(book1)
library.add_book(book2)

library.remove_book("Python Programming")
library.remove_book("Art of War")

# Added 'Python Programming' by John Doe to the library.
# Added 'Data Structures' by Jane Smith to the library.
# Removed 'Python Programming' from the library.
# Book 'Art of War' not found in the library.
# %%%%%%%%%%%%%%%%% 17 %%%%%%%%%%%%
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"{student.name} has been added to {self.name}")
        else:
            print("Invalid student object")

    def remove_student(self, student_name):
        for s in self.students:
            if s.name == student_name:
                self.students.remove(s)
                print(f"{student_name} has been removed from {self.name}")
                return
        print(f"{student_name} not found in {self.name}")

# Example usage
s1 = Student("John", 15)
s2 = Student("Alice", 16)

school1 = School("ABC High School")
school1.add_student(s1)  # Output: John has been added to ABC High School
school1.add_student(s2)  # Output: Alice has been added to ABC High School

print([s.name for s in school1.students])  # Output: ['John', 'Alice']

school1.remove_student("John")  # Output: John has been removed from ABC High School

print([s.name for s in school1.students])  # Output: ['Alice']

# %%%%%%%%%%%%%%%%  18  %%%%%%%%%%%%%%

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        if isinstance(person, Person):
            self.members.append(person)
            print(f"{person.name} has been added to {self.name}")
        else:
            print("Invalid person object")

    def remove_member(self, person_name):
        for p in self.members:
            if p.name == person_name:
                self.members.remove(p)
                print(f"{person_name} has been removed from {self.name}")
                return
        print(f"{person_name} not found in {self.name}")

# Example usage
p1 = Person("John", 25)
p2 = Person("Alice", 30)

team1 = Team("Football Team")
team1.add_member(p1)  # Output: John has been added to Football Team
team1.add_member(p2)  # Output: Alice has been added to Football Team

print([p.name for p in team1.members])  # Output: ['John', 'Alice']

team1.remove_member("John")  # Output: John has been removed from Football Team

print([p.name for p in team1.members])  # Output: ['Alice']

# %%%%%%%%%%% 19 %%%%%%%%%%%%

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            print(f"{employee.name} has been added to {self.name}")
        else:
            print("Invalid employee object")

    def remove_employee(self, employee_name):
        for e in self.employees:
            if e.name == employee_name:
                self.employees.remove(e)
                print(f"{employee_name} has been removed from {self.name}")
                return
        print(f"{employee_name} not found in {self.name}")

# Example usage
e1 = Employee("John", 25, 50000)
e2 = Employee("Alice", 30, 60000)

company1 = Company("ABC Company")
company1.add_employee(e1)  # Output: John has been added to ABC Company
company1.add_employee(e2)  # Output: Alice has been added to ABC Company

print([e.name for e in company1.employees])  # Output: ['John', 'Alice']

company1.remove_employee("John")  # Output: John has been removed from ABC Company

print([e.name for e in company1.employees])  # Output: ['Alice']

# %%%%%%%%%%%%%% 20 %%%%%%%%%%
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.name} has been added to {self.name}")
        else:
            print("Invalid animal object")

    def remove_animal(self, animal_name):
        for a in self.animals:
            if a.name == animal_name:
                self.animals.remove(a)
                print(f"{animal_name} has been removed from {self.name}")
                return
        print(f"{animal_name} not found in {self.name}")

# Example usage
a1 = Animal("Lion", "Panthera leo")
a2 = Animal("Tiger", "Panthera tigris")

zoo1 = Zoo("ABC Zoo")
zoo1.add_animal(a1)  # Output: Lion has been added to ABC Zoo
zoo1.add_animal(a2)  # Output: Tiger has been added to ABC Zoo

print([a.name for a in zoo1.animals])  # Output: ['Lion', 'Tiger']

zoo1.remove_animal("Lion")  # Output: Lion has been removed from ABC Zoo

print([a.name for a in zoo1.animals])  # Output: ['Tiger']


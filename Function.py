# def First():
#     {
#         print("Hello World")
#     }
# First()
# def User_input(Name):
#     print("Hello",Name)
#     User_input("Balvant")

# def fact(n):
#     if n==1 :
#         return 1
#     return n*fact(n-1)
# print(fact(5))


# def Fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     elif n==2:
#         return Fibo(n-1)+Fibo(n-2)


# class Animal:
#     def speak(self):
#         print("Animal make sound")
# class Dog(Animal):
#     def bark(self):
#         print("Dog bark")
# d=Dog()
# d.speak()
# d.bark()

# class Animal:
#     def sound(self):
#         print("some generic sound")
# class Cat:
#     def sound(self):
#         print("Meow!")
# a=Animal()
# c=Cat()
# c.sound()

# class BankAccount:
#     def__init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance +=amount

# class Student:
#     def __init__(self):
#         self.name = ""
#         self.roll_no = 0
#         self.marks = 0

#     def accept_details(self):
#         self.name = input("Enter student name: ")
#         self.roll_no = int(input("Enter roll number: "))
#         self.marks = float(input("Enter marks: "))

#     def display_details(self):
#         print("\n--- Student Details ---")
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)
#         print("Marks:", self.marks)


# # Creating object of Student class
# s1 = Student()

# # Accepting and displaying student details
# s1.accept_details()
# s1.display_details()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


# Create object
r = float(input("Enter radius of the circle: "))
c1 = Circle(r)

# Display results
print("Area of Circle:", c1.area())
print("Circumference of Circle:", c1.circumference())





    

    
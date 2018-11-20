class Lunch:

    def __init__(self, Customer, Employee):
        self.Customer = Customer
        self.Employee = Employee

    def order(self, foodName):
        self.Customer.placeOrder(foodName, self.Employee)

    def result(self):
        return self.Customer.food.name


class Customer:

    def __init__(self):
        self.food = None

    def placeOrder(self, foodName, employeeName):
        self.employee = employeeName
        self.food = self.employee.takeOrder(foodName)


class Employee:

    def takeOrder(self, foodName):
        return Food(foodName)


class Food:

    def __init__(self, name):
        self.name = name

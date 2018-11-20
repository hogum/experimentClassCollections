class Scene:

    def __init__(self, customerLine, parrotLine, clerkLine):
        self.customerLine = customerLine()
        self.parrotLine = parrotLine()
        self.clerkLine = clerkLine()

    def action(self):
        for line in [self.customerLine, self.parrotLine, self.clerkLine]:
            line.sayLine()


class SaySomething:

    def sayLine(self):
        self.noise = 'Says something'
        print(self.name, ' : ', self.noise)


class Customer(SaySomething):
    name = 'Customer'
    #def line(self):
    noise = 'That\'s one dead carrot'


class Parrot(SaySomething):
    name = 'Parrot'
    def line(self):
        pass


class Clerk(SaySomething):
    name = 'Clerk'

    #def line(self):
    noise = 'No it\'s not'

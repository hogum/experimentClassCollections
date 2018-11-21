class Scene:

    def __init__(self, customerLine, parrotLine, clerkLine):
        self.customerLine = customerLine()
        self.parrotLine = parrotLine()
        self.clerkLine = clerkLine()

    def action(self):

        return str('\n').join([self.customerLine.sayLine(),
                               self.parrotLine.sayLine(),
                               self.clerkLine.sayLine()])


class SaySomething:
    noise = 'Says something'

    def sayLine(self):
        # print(self.name, ' : ', self.noise)
        return self.name + ' : ' + self.noise


class Customer(SaySomething):
    name = 'Customer'
    noise = 'That\'s one dead carrot'


class Parrot(SaySomething):
    name = 'Parrot'

    def line(self):
        pass


class Clerk(SaySomething):
    name = 'Clerk'
    noise = 'No it\'s not'

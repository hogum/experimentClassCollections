import unittest

from lunch_compsition import Lunch, Customer, Employee


class TestComposition(unittest.TestCase):

    def setUp(self):
        self.food = 'Burritos'
        self.waiter = Employee()
        self.eater = Customer()
        self.orderFood = Lunch(self.eater, self.waiter)

    def test_result(self):
        self.orderFood.order(self.food)

        self.assertEqual(self.orderFood.result(), 'Burritos')

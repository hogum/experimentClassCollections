import unittest


from parrot_sketch import Scene, Customer, Parrot, Clerk


class TestScene(unittest.TestCase):

    def setUp(self):
        self.clerk = Clerk
        self.customer = Customer
        self.parrot = Parrot
        self.start_scene = Scene(self.customer, self.parrot, self.clerk)

    def test_scene_action(self):
        res = self.start_scene.action()

        self.assertIsInstance(res, str)

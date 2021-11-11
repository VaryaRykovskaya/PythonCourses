import unittest
import homework5_Funkcii


class MyTestCase(unittest.TestCase):
    """Calc test: """

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up some stuff for [" + self.shortDescription() + "]")
        print("--------------------------")

    def tearDown(self):
        """Tear Down Method!"""
        print("--------------------------")
        print("Cleaning mess after [" + self.shortDescription() + "]")
        print("--------------------------")

    def test_greater(self):
        """ area of circle greater than 28 """
        self.assertGreater(homework5_Funkcii.area_circle(3), 28)


    def test_none(self):
        """ function just print and doesn't return anything """
        self.assertIsNone(homework5_Funkcii.hello_only())


    def test_true(self):
        """ function checks if a is greater than b"""
        self.assertTrue(homework5_Funkcii.true_false(5, 3))


if __name__ == '__main__':
    unittest.main()

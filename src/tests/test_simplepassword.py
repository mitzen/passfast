import unittest
from randompass import RandomPasswordGenerator

class RandomPasswordTest(unittest.TestCase):
    
    def test_random_password_not_empty(self):
        result = RandomPasswordGenerator().generate_password()
        self.assertIsNotNone(result)

    def test_random_password_length(self):
        result = RandomPasswordGenerator().generate_password()
        self.assertEqual(len(result), 20)

    def test_custom_password_length(self):
        result = RandomPasswordGenerator().generate_password(25)
        self.assertEqual(len(result), 25)

print(__name__)

if __name__ == '__main__':
    unittest.main()


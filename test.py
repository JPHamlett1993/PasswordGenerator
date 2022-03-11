from email.charset import Charset
import unittest

from passwordModule import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_password_generator_len(self):
        self.assertEqual(len(generate_password(8, True, True, True)), 8)
        self.assertEqual(len(generate_password(-1, True, True, True)), 0)
        self.assertEqual(len(generate_password(0, True, True, True)), 0)
    
    def test_password_generator_chars(self):
        self.assertTrue(any(char.isalpha() for char in generate_password(8, True, False, False)))
    
    def test_password_generator_ints(self):
        self.assertTrue(any(char.isdigit() for char in generate_password(8, False, True, False)))

    def test_password_generator_specials(self):
        self.assertTrue(any(char in "!@#$%^&*()_+" for char in generate_password(8, False, False, True)))

if __name__ == '__main__':
    unittest.main()
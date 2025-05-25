import unittest
from Encripted_password import *

class MyTestCase(unittest.TestCase):
    def test_encrpt_password(self):
        password =  EncryptedPassword("Hello. World")
        self.assertEqual("Uryyb. Jbeyq", password.encrypt())
         # add assertion here

    def test_decrpt_password(self):
        password =  EncryptedPassword("Uryyb. Jbeyq")
        self.assertEqual("Hello. World", password.decrypt())


if __name__ == '__main__':
    unittest.main()

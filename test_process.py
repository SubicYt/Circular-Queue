import unittest
from process import *

class TestProcess(unittest.TestCase):
    
    def test_init_name(self):
        p1 = Process("send_mail")
        p2 = Process("create_password", 3000)
        p3 = Process("send_mail")

        self.assertEqual(p1.pid, "send_mail")
        self.assertEqual(p3.pid,"send_mail")
        self.assertEqual(p2.pid, "create_password")

    def test_init_name_and_cycles(self):
        p1 = Process("send_mail")
        p2 = Process("create_password", 3000)
        p3 = Process("send_mail")

        self.assertEqual(p1.cycles, 100)
        self.assertEqual(p3.cycles,100)
        self.assertEqual(p2.cycles, 3000)

    def test_eq(self):
        p1 = Process("send_mail")
        p2 = Process("create_password", 3000)
        p3 = Process("send_mail")

        self.assertEqual(p1, p3)
        self.assertNotEqual(p3, p2)

    def test_repr(self):
        p1 = Process("send_mail")
        p2 = Process("create_password", 3000)
        p3 = Process("send_mail")
        self.assertEqual(repr(p2), "create_password, 3000")
        self.assertEqual(repr(p3),repr(p1))
        self.assertNotEqual(repr(p2),repr(p1))

if __name__ == "__main__":
    unittest.main() 


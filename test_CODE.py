from logging import root
import unittest
from CODE import Bill_App
from tkinter import*
root=Tk()
a=Bill_App(root)

class Bill_App(unittest.TestCase):
    def test_total(self):
        self.assertIsNot(a.testing(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

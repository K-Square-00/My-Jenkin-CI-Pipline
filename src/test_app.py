import unittest
from app import Student

class testStudent(unittest.TestCase):
    def test_get_name(self):
        jack = Student("jack",18)
        self.assertEqual(jack.get_name(), "jack")



if __name__ == "__main__":
    unittest.main()
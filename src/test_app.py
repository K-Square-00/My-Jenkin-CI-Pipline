import unittest
from app import Student

class testStudent(unittest.TestCase):
    def test_get_name(self):
        jack = Student("jack",18)
        self.assertEqual(jack.get_name(), "jack")
    
    def test_get_age(self):
        jack = Student("jack",18)
        self.assertEqual(jack.get_age(),18)



if __name__ == "__main__":
    unittest.main()
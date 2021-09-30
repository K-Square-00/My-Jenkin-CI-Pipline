import unittest
from app import Student

class testStudent(unittest.TestCase):
    def test_get_name(self):
        jack = Student("jack",18)
        self.assertEqual(jack.get_name(), "jack")
    
    def test_get_age(self):
        jack = Student("jack",18)
        self.assertEqual(jack.get_age(),18)

    def test_get_skill(self):
        jack = Student("jack",18)
        self.assertEqual(jack.get_skills(),['python'])   

    def test_add_skill(self):
        jack = Student("jack",18)
        self.test_add_skill('java')
        self.assertEqual(jack.get_skills(),['python','java'])   

if __name__ == "__main__":
    unittest.main()
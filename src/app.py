import time


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = ['python']

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_skills(self):
        return self.skills

    def add_skill(self,skill):
        pass

    def get_time(self):
        return "Welcome!!! ", time.localtime

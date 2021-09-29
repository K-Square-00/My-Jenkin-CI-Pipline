#import flask
import time

class Student():
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.skills = []
    

    def get_name(self):
        return self.name

    def get_age(self):
        pass

    def get_skills(self):
        pass

#app = flask.Flask(__name__)


#@app.route("/")
#def index():
#    return "Welcome!!! ", time.localtime

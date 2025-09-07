'''
    Employee class with getter and setters for 'id' and 'name'.
'''

class Employee():
    def __init__(self, name, an_id):
        self.name = name
        self.an_id = an_id

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_id(self, new_id):
        self.an_id = new_id

    def get_id(self):
        return self.an_id

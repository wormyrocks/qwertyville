import constants as c

class Person(object):
  def __init__(self):
    self.first = self.choose_name(False)
    self.last = self.choose_name(True)
  def choose_name(self, is_last):
     pass    

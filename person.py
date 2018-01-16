class Person(object):

  def __init__(self):
    print("HI");
    self.first = self.choose_name(False)
    self.last = self.choose_name(True)

  def choose_name(self, is_last):
     pass    

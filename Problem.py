import random

class Problem(object):
  def __init__(self, operation, bottom_range, top_range):
    self.operation = operation
    self.first_num = random.randint(bottom_range, top_range)
    self.second_num = random.randint(bottom_range, top_range)

  def printproblem(self, operation):
    if operation == "add":
      print "%s + %s" % (self.first_num, self.second_num)
    elif operation = "subtract":  
      print "%s - %s" % (self.first_num, self.second_num)
    elif operation = "multiply":
      print "%s x %s" % (self.first_num, self.second_num)
    else:
      print "%s / %s" % (self.first_num, self.second_num)

import random

class Problem(object):
  def __init__(self, operation, bottom_range, top_range):
    self.operation = operation
    self.first_num = random.randint(bottom_range, top_range)
    self.second_num = random.randint(bottom_range, top_range)
  
  def answerproblem(self):
    if self.operation == 1:
      return self.first_num + self.second_num
    elif self.operation == 2:  
      return self.first_num - self.second_num
    elif self.operation == 3:
      return self.first_num * self.second_num
    else:
      return "Not a valid operation."

  def printproblem(self):
    if self.operation == "add":
      print "%s + %s" % (self.first_num, self.second_num)
    elif self.operation == "subtract":  
      print "%s - %s" % (self.first_num, self.second_num)
    elif self.operation == "multiply":
      print "%s x %s" % (self.first_num, self.second_num)
    else:
      print "Not a valid operation,"

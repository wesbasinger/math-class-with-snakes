import random
from Problem import *

class LevelOne(Problem):

  def __init__(self,operation):
    self.operation = operation
    self.first_num = random.randint(0,10)
    self.second_num = random.randint(0,10)



import random
from Problem import *

class LevelTwo(Problem):

  def __init__(self,operation):
    self.operation = operation
    self.first_num = random.randint(0,20)
    self.second_num = random.randint(0,20)



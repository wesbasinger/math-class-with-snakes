import random
from Problem import *

class LevelThree(Problem):

  def __init__(self,operation):
    self.operation = operation
    self.first_num = random.randint(-20,20)
    self.second_num = random.randint(-20,20)




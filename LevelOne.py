import random
from Problem import *
from Player import Player

class LevelOne(Problem):

  def __init__(self,operation):
    self.operation = operation
    self.first_num = random.randint(0,10)
    self.second_num = random.randint(0,10)
    

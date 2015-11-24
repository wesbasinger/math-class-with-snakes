import os

class Player(object):

  def __init__ (self, name):
    self.name = name
    self.score = 0
    path = '/Users/teacher/Desktop/LPTHW/Second_Half/class_practice/math_class_with_snakes/logs/'
    filename = self.name + "log" + ".txt"
    filename = os.path.join(path, filename)
    self.log = open(filename, "w")

  def getscore(self):
    return self.score

  def setscore(self, points):
    self.score += points



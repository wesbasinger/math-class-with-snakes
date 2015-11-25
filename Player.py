import os


class Player(object):

  def __init__ (self, name):
    self.name = name # set player name
    self.score = 0 # initialize score to zero
    path = '/Users/teacher/Desktop/LPTHW/Second_Half/class_practice/math_class_with_snakes/logs'
    filename = self.name + "_log.bin"
    filename = os.path.join(path, filename)
    f  = open( filename, "wb")
    f.write("0")
    f.close()

  def getscore(self):
    path = '/Users/teacher/Desktop/LPTHW/Second_Half/class_practice/math_class_with_snakes/logs'
    filename = self.name + "_log.bin"
    filename = os.path.join(path, filename)
    f = open( filename, "rb")
    print f.read()
    f.close()

  def setscore(self, points):
    self.score += points
    path = '/Users/teacher/Desktop/LPTHW/Second_Half/class_practice/math_class_with_snakes/logs'
    filename = self.name + "_log.bin"
    filename = os.path.join(path, filename)
    f = open(filename, "wb")
    f.write(str(self.score))
    f.close()
"""
This doesn't work at all    
def initial_write(name, score):
  # first the dictionary file is opened
  f = open("scores.txt", "r+")
  #then the dictionary is extracted
  dc = [] #empty container for the dictionary
  with f as inf:
    for line in inf:
      dc.append(eval(line))
  wd = dc[0]
  wd[name] = score
  print wd
  f.close()
"""

from Player import *

class Log(Player):

  def __init__(self, name):
    f  = open(self.name+"logfile.txt","r+")
    f.write("This is a logfile for somebody")
    f.close()



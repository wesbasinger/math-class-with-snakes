import os
import re

class Scoreboard(object):
  def __init__(self):
    pass

  def importscores(self):
    scores_container = {}
    for root, dirs, files in os.walk('/Users/teacher/Desktop/LPTHW/Second_Half/class_practice/math_class_with_snakes/logs'):
      for f in files:
        fopen = open("/Users/teacher/Desktop/LPTHW/Second_Half/class_practice/math_class_with_snakes/logs/"+f, "rb")
	data = fopen.read()
        scores_container[f] = data
        fopen.close()
    name_container = {}
    for key in scores_container:
      split_name = key.split("_")
      first_name = split_name[0].capitalize()
      name_container[key] = first_name
    for key in scores_container:
      print "Name: %s   Score: %s" % (name_container[key], scores_container[key])

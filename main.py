import sys
import os
from Player import Player
from LevelOne import LevelOne
from LevelTwo import LevelTwo
from LevelThree import LevelThree
from Scoreboard import Scoreboard

""" # Not sure if I need this
def find(name, path):
  for root, dirs, files in os.walk(path):
    if name in files:
      return os.path.join(root,name)
"""
def main():
  print "-----CURRENT SCOREBOARD-----"
  scoreboard = Scoreboard()
  scoreboard.importscores()
  #first log the player in or create them if they don't exist
  prompt_name = raw_input(str("What is your name? "))
  prompt_name_lower = prompt_name.lower()
  for root, dirs, files in os.walk('/Users/teacher/Desktop/LPTHW/Second_Half/class_practice/math_class_with_snakes/logs'):
    if (prompt_name_lower + "_log.bin") in files:
      print "Hello, %s, welcome back - you are logged in!\n" % prompt_name_lower.capitalize()
      f = open('/Users/teacher/Desktop/LPTHW/Second_Half/class_practice/math_class_with_snakes/logs/' + prompt_name_lower + "_log.bin", "rb")
      saved_score = int(f.read())
      f.close()
      prompt_name_lower = Player(prompt_name_lower)
      prompt_name_lower.setscore(saved_score)
      print "Your current score is %s.\n" % saved_score
      problem_loop(prompt_name_lower)
    else:
      print "We'll set you up a new user!\n"
      prompt_name_lower = Player(prompt_name_lower)
    while True:
      print "'any key' for new problem 'q' for quit\n"
      choice = str(raw_input())
      if choice == "q":
        #print "Bye, your score is %s" % prompt_name_lower.getscore()
        sys.exit(0)
      else:
        problem_loop(prompt_name_lower)


def problem_loop(prompt_name_lower):

  prompt_level = int(input("Pick your level 1 2 3 >>>"))
  prompt_operation = int(input("Pick your operation (1)add (2)subtract (3)multiply >>>"))
  
  if prompt_level == 1:
    cur_prob = LevelOne(prompt_operation)
    cur_prob.printproblem()
  elif prompt_level == 2:
    cur_prob = LevelTwo(prompt_operation)
    cur_prob.printproblem()
  elif prompt_level == 3:
    cur_prob = LevelThree(prompt_operation)
    cur_prob.printproblem()
  else:
    print prompt_level
    print prompt_operation
  print "\n"
  prompt_answer = int(input("ANSWER >>> "))
  if prompt_answer == cur_prob.answerproblem():
    print "You got it!"
    if prompt_level == 1:
      prompt_name_lower.setscore(100)
    elif prompt_level == 2:
      prompt_name_lower.setscore(200)
    else:
      prompt_name_lower.setscore(300)
  else:
    print "Better luck next time!"
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()



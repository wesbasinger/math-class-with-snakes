import os
from Player import Player
from LevelOne import LevelOne
from LevelTwo import LevelTwo
from LevelThree import LevelThree


def find(name, path):
  for root, dirs, files in os.walk(path):
    if name in files:
      return os.path.join(root,name)

def main():

  #first log the player in or create them if they don't exist
  prompt_name = raw_input(str("What is your name? "))
  prompt_name_lower = prompt_name.lower()
  for root, dirs, files in os.walk('/Users/teacher/Desktop/LPTHW/Second_Half/class_practice/math_class_with_snakes/logs'):
    print files
    if (prompt_name_lower + "_log.bin") in files:
      print "Hello, %s, welcome back - you are logged in!" % prompt_name_lower.capitalize()
      f = open('/Users/teacher/Desktop/LPTHW/Second_Half/class_practice/math_class_with_snakes/logs/' + prompt_name_lower + "_log.bin", "rb")
      saved_score = int(f.read())
      f.close()
      prompt_name_lower = Player(prompt_name_lower)
      prompt_name_lower.setscore(saved_score)
      print "Your current score is %s." % saved_score
    else:
      print "We'll set you up a new user!"
  problem_loop()

def problem_loop():

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

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()



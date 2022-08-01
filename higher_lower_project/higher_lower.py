# importing the logo
from art import logo, vs
import random
from game_data import data
import os

# random a choice from the game data
def generated_choice(data):
  """ This function is to generate a random choice."""
  # print(random.choice(data))
  randomed = random.choice(data)
  return randomed

# function to obtain the correct answer - the value given is the number
def correct_answer(options):
  if options['a']['follower_count'] > options['b']['follower_count']:
    return options['a']
  else:
    return options['b']

def wrong_answer(options):
  if options['a']['follower_count'] > options['b']['follower_count']:
    return options['b']
  else:
    return options['a']

#comparsion function to compare between a and b
def compare(guessed_answer, correct_answer, score):
  # a method to extract the name
  if options[guessed_answer] != correct_answer:
    print(f"Sorry, that's wrong. Final score: {score}")
    # need to return something here
    return False
  else:
    score += 1
    print(f"You're right! Current score: {score}")
    return score

end_game = False
score = 0
# options = []
options = {}

print(logo)
# main game loop
while not end_game:
  if score > 0:
    # first_selection = wrong_answer(options)
    first_selection = second_selection
  else:
    first_selection = generated_choice(data)
  options.clear()
  print(f"Compare A: {first_selection['name']}, a {first_selection['description']}, from {first_selection['country']}")
  print(vs)
  second_selection = generated_choice(data)
  while first_selection == second_selection:
    second_selection = generated_choice(data)
  print(f"Compare B: {second_selection['name']}, a {second_selection['description']}, from {second_selection['country']}")
  options = {
    'a': first_selection,
    'b': second_selection,
  }

  # print(correct_answer(options))
  # need to create a dictionary for both options a and b - should be able to create another dictionary within a dictionary

  # print(options[actual_answer])
  # compare B:
  answer = input("Who has more followers? Type 'A or 'B': ").lower()

  os.system('clear')
  print(logo)
  score = compare(answer, correct_answer(options), score)
  # print(score)

  if score == False:
    end_game = True
  

  

# else:
  # print(f"Sorry, that's wrong. Final score: {score}")
  
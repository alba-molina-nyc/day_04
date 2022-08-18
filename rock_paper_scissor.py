import random

# random choose between rock paper scissor and then compare choice against my choice based on the rules of rock paper or scissor determine whether won or lost

# TODO: come back and finish
"""Instructions
Make a rock, paper, scissors game.

Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player."""

def rock_paper_scissors():
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

random = random.randint(0, 2)

choice = input('what do you choose, Type 0 for ROCK, 1 for PAPER and 2 for SCISSORS ')

print(random, 'random')
if random == 0 and choice == 0:
    print('tied both picked rock')
elif random == 1 and choice == 0:
    print('you win, you picked {choice} over {random}')



if __name__ == '__main__':
    rock_paper_scissors()
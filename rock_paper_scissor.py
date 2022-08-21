import random

# random choose between rock paper scissor and then compare choice against my choice based on the rules of rock paper or scissor determine whether won or lost

# TODO: come back and finish debugging bc when you inout # greater than 2 then it gives err
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
    game_imgs = [rock, paper, scissors]
    user_choice = int(input('what do you choose? | Type: 0 for 🪨 | 1 for 📜 | 2 for ✂️ | '))
    print(f'👤 {game_imgs[user_choice]}')

    computer_choice = random.randint(0, 2)
    print(f'🤖 Chose: {game_imgs[computer_choice]}')

    # print(f'{computer_choice} 🤖')
    # print(f'{user_choice} 👤')

    if user_choice >= 3 or user_choice <0:
        print('❌you typed an invalid number❌')
    elif user_choice == 0 and computer_choice == 2:
        print(f'👤You win🏆')
    elif computer_choice == 0 and user_choice == 2:
        print(f'👤You lose🥈')
    elif computer_choice > user_choice:
        print('you loose🥈')
    elif user_choice > computer_choice:
        print('you win🏆')
    elif computer_choice == user_choice:
        print('its a draw')
    
    
 
        
    




if __name__ == '__main__':
    rock_paper_scissors()
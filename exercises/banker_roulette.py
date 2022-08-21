import random

def banker_roulette():
    names_string = input('Give me everybodys names separated by commas: ')
    names = names_string.split(', ')
    num_items = len(names)
    random_choice = random.randint(0, num_items - 1)
    person_who_will_pay = random.choice(names)
    print(person_who_will_pay + "is going to buy the meal today")

if __name__ == '__main__':
    banker_roulette()
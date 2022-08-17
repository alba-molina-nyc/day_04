def banker_roulette():
    names = input('Give me everybodys names separated by commas: ')
    print(f'{names}')
    print(type(names))
    
    names = names.split(', ')
    print(f'{names}')
    print(type(names))
    pass


if __name__ == '__main__':
    banker_roulette()
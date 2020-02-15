import random


def takeShower():
    print('showering')
    return 'Showering'


def eatBreakfast():
    meal = cookFood()
    print(f'eating {meal}')
    return f'eating {meal}'


def cookFood():
    items = ['Oatmeal', 'Eggs', 'Protein Shake']
    num = random.randint(1, len(items))
    meal = items[num-1]
    print(meal)
    return meal


def wakeUp():
    takeShower()
    eatBreakfast()
    print('Ok ready to go to work')


wakeUp()

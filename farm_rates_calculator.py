items = []
'''items = [[name, value, seconds/item], [name, value, seconds/item]]'''

def welcome():
    print('Welcome to the farm rates calculator!')

def main():
    welcome()
    while True:
        print('')
        print('Please enter an index:')
        print('1. Enter the time spent & items produced by a farm')
        print('2. print the items/time for each item produced by the farm')
        print('3. print the time/item for each item produced by the farm')
        print('4. print the time/various quantities produced by the farm for a specific item')
        index = integer('index: ')
        print('')
        if index == 1:
            global total_time
            total_time = enter_time()
            print(make_time_string(translate_time(total_time)))
            get_items()
        if index == 2:
            print_items_per_time()
        if index == 3:
            print_time_per_items()
        if index == 4:
            print_full_amounts()

def get_items():
    n_items = integer('How many items do you want to calculate the rates for? ')
    for n in range(n_items):
        name = input(f'What is the name of item {n+1}? ')
        rows = integer(f'How many rows of {name} were produced? ')
        stacks = integer(f'How many additional stacks of {name} were produced? ')
        remainder = integer(f'How many additional {name} were produced? ')
        number = 9*64*rows + 64*stacks + remainder
        seconds_per_item = total_time / number
        items.append([name, number, seconds_per_item])

def enter_time():
    print('Please enter the amount of time:')
    hours = floating('hours: ')
    minutes = floating('minutes: ')
    seconds = floating('seconds: ')
    total_time = hours*3600 + minutes*60 + seconds # total time given in seconds
    return total_time

def translate_time(total_time):
    hours = round(total_time//3600)
    total_time -= 3600*hours
    minutes = round(total_time//60)
    total_time -= 60*minutes
    seconds = round(total_time, 2)
    return hours, minutes, seconds

def make_time_string(time):
    hours = time[0]
    minutes = time[1]
    seconds = time[2]
    if hours != 0:
        return f'{hours} hours + {minutes} minutes + {seconds} seconds'
    elif minutes!= 0:
        return f'{minutes} minutes + {seconds} seconds'
    else:
        return f'{seconds} seconds'

def print_items_per_time():
    total_seconds = enter_time()
    time_string = make_time_string(translate_time(enter_time))
    print(f'During the course of {time_string}, the farm produces:')
    for n in range(len(items)):
        name = items[n][0]
        seconds_per_item = items[n][2]
        number = total_seconds * seconds_per_item
        print(f'{number} {name}')

def print_time_per_items():
    print('Enter how many of each item you want the farm to produce')
    amount = integer('amount: ')
    print(f'This is how long it takes for the farm to produce {amount} of each item:')
    for n in range(len(items)):
        name = items[n][0]
        seconds_per_item = items[n][2]
        seconds = amount * seconds_per_item
        time_string = make_time_string(translate_time(seconds))
        print(f'{amount} x {name}: {time_string}')

def print_full_amounts():
    n = choose_item_index()
    name = items[n][0]
    seconds_per_item = items[n][2]
    print(f'\nThis is the amount of time it takes for this farm to produce various amounts of {name}:')
    print(f'1 Stack:             {make_time_string(translate_time(seconds_per_item * 64))}')
    print(f'1 Row:               {make_time_string(translate_time(seconds_per_item * 64 * 9))}')
    print(f'1 Chest/Shulker Box: {make_time_string(translate_time(seconds_per_item * 64 * 9 * 3))}')
    print(f'1 Double Chest:      {make_time_string(translate_time(seconds_per_item * 64 * 9 * 6))}')
    print(f'5 Double Chest:      {make_time_string(translate_time(seconds_per_item * 64 * 9 * 6 * 5))}')



def integer(question):
    while True:
        try:
            answer = input(question)
            return int(answer)

        except TypeError as type_err:
                print(f"The number you entered {type_err} you entered is not a valid integer")

        except ValueError as val_err:
            print(f"The number you entered {val_err}, has non-number characters")

def floating(question):
    while True:
        try:
            answer = input(question)
            return float(answer)
        except TypeError as type_err:
                print(f"The number you entered {type_err} you entered is not a valid number")
        except ValueError as val_err:
            print(f"The number you entered {val_err}, has non-number characters")

def choose_item_index():
    while True:
        try:
            print("Please enter the index of one of the items:")
            for n in range(len(items)):
                print(f'{n + 1}. {items[n][0]}')
            index = integer("Index: ") - 1
            if index > len(items):
                print(f"Sorry, that's not a valid index. Please enter an integer from 1 to {len(items)}")
                choose_item_index()
            else:
                return index - 1
        except TypeError as type_err:
            print(f'Type Error: {type_err}')
            print(f"The index you entered {index} is not a valid index")
        except ValueError as val_err:
            print(f'Value Error: {val_err}')
            print(f"The index you entered {index}, have non-number characters")

main()
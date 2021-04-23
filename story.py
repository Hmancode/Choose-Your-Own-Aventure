import sys
from time import sleep


def game(player, characters, items):
    output_0 = paths_0(player, characters, items)
    if output_0 == 'paths_1':
        paths_1(player, characters, items)
    elif output_0 == 'paths_2':
        paths_2(player, characters, items)


def paths_0(player, characters, items):
    write_string("----------The Castle's Conflict----------")
    sleep(.1) #Should be 5, .1 for debug
    write_file('paths_0_1')
    write_string(" ... What is your name?")
    player.name = input(" ")
    write_string("Hey, %s!\n" % player.name)
    write_file('paths_0_2')
    sleep(1)
    write_file('paths_0_3')
    options = ["Fight", "Blacksmith"] 
    prep = "Do you wish to fight him for the gear, or go to the blacksmith?"
    output_0_3 = choice(prep, options)
    if output_0_3 == options[0].lower():
        battle(player, characters['guard'], 1)
        player.inventory_add(items['guard_sword'])
        write_string("You don the armor and weild the weapons of the guard.")
    write_file("paths_0_4")
    options2 = ['Duties', 'Gear']
    prep = "Which do you want to persue?"
    output_0_4 = choice(prep, options2)
    if output_0_4 == options2[0].lower():
        return 'paths_1'
    elif output_0_4 == options2[1].lower():
        return 'paths_2'

def paths_1(player, characters, items): #Castel/duties
    write_file("paths_1_0")
    write_string(player.name + '"\nThis has never happend before, you are never questioned. Are these guards going to take advantage of your weakness for the rebellion? ')
    options = ['Flee', 'Fight']
    prep = "What do you do?"
    output_1_0 = choice(prep, options)
    if output_1_0 == options[0].lower():
        write_file("paths_1_1")
    if output_1_0 == options[1].lower():
        characters['guard'].inventory_add(items['sheild'])
        battle(player, characters['guard'], 2)



def paths_2(player,character,items): #find weapon
    pass

def paths_3(player, characters, items): #merge 1 and 2 - bandit
    pass



def choice(prep, options):
    go = True
    string_list = ", ".join(options)
    string = prep + ' [' + string_list + ']:'
    new_options = []
    for element in options:
        new_options.append(element.lower())
    while go:        
        write_string(string)
        choice = input(' ').lower()
        if choice in new_options:
            go = False
        else:
            write_string('Please input a vaild argument --- ')
    return choice

def battle(side1, side2, side_2_heals_at):
    from game import battle as battle_ver1
    return battle_ver1(side1, side2, side_2_heals_at)

def write_string(text):
    for line in text:
            for char in line:
                sleep(.0001) #Should be .6 - Lowered for decoding
                sys.stdout.write(char)
                sys.stdout.flush()
def write_file(file_name):
    file_name = "texts/" + file_name + ".txt"
    with open(file_name, 'r') as text:
        for line in text:
            for char in line:
                sleep(.0001) #Should be .6 - Lowered for decoding
                sys.stdout.write(char)
                sys.stdout.flush()
    print(' ')
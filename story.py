import sys
from time import sleep


def game(player, characters, items):
    intro(player)
    paths_0(player, items)

def intro(player):
    write_file('intro_text.txt')
    player.name = input(" ... What is your name? ")

def paths_0(player, items):
    write_string("Hey, %s!\n" % player.name)
    write_file('paths_0.txt')
    options = [items['sword'].name, items['sheild'].name, items['apple'].name]
    prep = "What item would you like to have?"
    thing = choice(prep, options)
    write_string("You now have a %s -- Luck: %i" % (thing, items[thing].luck))


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

def write_string(text):
    for line in text:
            for char in line:
                sleep(.01) #Should be .6 - Lowered for decoding
                sys.stdout.write(char)
                sys.stdout.flush()
def write_file(file_name):
    with open(file_name, 'r') as text:
        for line in text:
            for char in line:
                sleep(.01) #Should be .6 - Lowered for decoding
                sys.stdout.write(char)
                sys.stdout.flush()
    print(' ')
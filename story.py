import sys
from time import sleep

def game(player):
    intro(player)
    paths_0(player)

def intro(player):
    write_file('intro_text.txt')
    player.name = input("\n ... What is your name? ")

def paths_0(player):
    write_string("Hey, %s!" % player.name)
    write_file('paths_0.txt')



def write_string(text):
    for line in text:
            for char in line:
                sleep(.06)
                sys.stdout.write(char)
                sys.stdout.flush()
def write_file(file_name):
    with open(file_name, 'r') as text:
        for line in text:
            for char in line:
                sleep(.06)
                sys.stdout.write(char)
                sys.stdout.flush()
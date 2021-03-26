import sys
from time import sleep

def start():
    intro_text = open("intro_text.txt", 'r')
    write(intro_text)

def write(text):
    for line in text:
        for char in line:
            sleep(.1)
            sys.stdout.write(char)
            sys.stdout.flush()

start()
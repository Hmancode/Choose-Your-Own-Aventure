class character:
    def __init__(self, name, strength, health, level):
        self.name = name
        self.strength = strength
        self.health = health
        self.level = level
    
    def is_dead(self):
        if self.health < 0:
            return True
    def get_level(self):
        return self.level

class item:
    def __init__(self, type, attack, defense, luck):
        self.type = type
        self.attack = attack
        self.defense = defense
        self.luck = luck


def start():
    player = character(name, strength, health, level)
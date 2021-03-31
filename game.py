import story

def start():
    player = character('name', 1, 1, 0, 5, 0)
    items = define_items()
    characters = define_characters()
    story.game(player, characters, items)


def define_items():
    items = {
        "sword":item("Sword", 'weapon', 2, 4, 1, 1),
        "sheild":item("Sheild", 'weapon', 0, 10, 3, 2),
        "apple":item("Apple", 'food', 0, 0, 9, 5),
    }
    return items

def define_characters():
    characters = {
        "meanie":character("Meanie", 20, 10, 3, 2, 0)
    }
    return characters

class character:
    def __init__(self, name, strength, health, level, level_stats_base, xp):
        self.name = name
        self.strength = strength
        self.health = health
        self.level = level
        self.level_stats_base = level_stats_base
        self.xp = xp
    def is_dead(self):
        if self.health < 0:
            return True        
    def level_up(self):
        while self.xp > self.level * 10:
            spent_xp = self.level * 10
            self.xp = self.xp - spent_xp
            self.level = self.level + 1
            print("\n***LEVEL UP***")
            print("**%s has reached level %i**" % (self.name, self.level))
            self.update_stats()
    def update_stats(self):
        self.strength = self.level * self.level_stats_base
        self.health = self.level * self.level_stats_base
        print("*Strength: %i --- Health: %i*" % (self.strength, self.health))
class item:
    def __init__(self, name, type, attack, defense, luck, xp_bonus):
        self.name = name
        self.type = type
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.xp_bonus = xp_bonus

#Make a weapon subclass of Item

start()
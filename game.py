import story

def start():
    player = character('name', 1, 1, 0, 5, 0)
    #story.game(player)
    print("\n ... \n")
    player.level_up()

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
    def __init__(self, type, attack, defense, luck, xp_bonus):
        self.type = type
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.xp_bonus = xp_bonus

start()
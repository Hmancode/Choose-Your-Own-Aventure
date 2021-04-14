import sys, random
from time import sleep


def start():
    player = character('name', {}, 1, 1, False, 0, 5, True, 5, 0)
    items = define_items()
    characters = define_characters()
    return player, characters, items


def define_items():
    items = {
        "sword":item("Sword", 'weapon', 7, 4, 1, 1),
        "sheild":item("Sheild", 'weapon', 0, 3, 3, 2),
        "gator tooth":item("Gator Tooth", 'weapon', 4, 0, 7, 3),
        "crystal":item("Crystal", 'artifact', 0, 0, 9, 5),
    }
    return items

def define_characters():
    characters = {
        "meanie":character("Meanie", {}, 1, 10, False, 3, 2, False, 5, 5),
    }
    return characters

class character:
    def __init__(self, name, inventory, strength, health, is_dead, level, level_stats_base, is_player, max_items, xp):
        self.name = name
        self.inventory = inventory
        self.strength = strength
        self.health = health
        self.is_dead = is_dead
        self.level = level
        self.level_stats_base = level_stats_base
        self.is_player = is_player
        self.max_items = max_items
        self.xp = xp       
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
        self.max_items = 5 + (self.level) * 1
        print("*Strength: %i --- Health: %i*" % (self.strength, self.health))
    def inventory_add(self, item):
        self.max_items = 1
        go = True
        while go:
            if len(self.inventory) > self.max_items:
                write_string("You cannot carry all that, you must remove somthing first.\n")
                self.inventory_edit()
                if len(self.inventory) > self.max_items:
                    con = input("Are you sure you do not want to continue without adding {}? [y/n]: ".format(item.name))
                    if con == 'y':
                        return
                    elif con == 'n':
                        pass
                    else:
                        write_string('Please input a vaild argument --- ')
                else:
                    go = False
            else:
                go = False
        self.inventory[item.name.lower()] = item
        self.inventory_print()
        return
    def inventory_print(self):
        print("\nInventory:")
        i = 1
        for item in self.inventory:
            print("{} - {}".format(i, self.inventory[item].name))
            i += 1
        print("\n")
    def inventory_edit(self):
        go = True
        while go:
            self.inventory_print()
            item = input("To exit, enter 'exit'. To view item details, enter item: ").lower()
            if item in self.inventory:
                go = False
                dic = self.inventory[item].__dict__
                print('\n')
                for element in dic:
                    print("{}: {}".format(element, dic[element]))
            elif item == 'exit':
                go = False
                return
            else:
                write_string('Please input a vaild argument --- ')
                continue
            run = True
            while run:
                request = input("Would you like to remove this item? [y/n]: ")
                if request == 'y':
                    run = False
                    go = True
                    del self.inventory[item]
                elif request == 'n':
                    run = False
                    go = True
                    pass
                else:
                    write_string('\nPlease input a vaild argument --- ')
    def attack_val(self):
        attack_bonus = 0
        for item in self.inventory:
            if self.inventory[item].type == 'weapon':
                val = self.inventory[item].attack * self.strength
                val2 = random.choice(range(self.inventory[item].luck)) 
                attack_bonus = attack_bonus + val + val2
        return attack_bonus + self.strength
    def defense_val(self):
            defense_bonus = 0
            for item in self.inventory:
                if self.inventory[item].type == 'weapon': 
                    val = self.inventory[item].defense * self.health
                    val2 = random.choice(range(self.inventory[item].luck)) 
                    defense_bonus = defense_bonus + val + val2
            return defense_bonus + self.health
    def battle_luck(self):
        val = 0
        for item in self.inventory:
            if self.inventory[item].type == 'weapon':
                val2 = random.choice(range(self.inventory[item].luck)) * self.strength
                val = val + val2
        return val
    def battle_xp(self, opponent):
        val = 1
        for item in self.inventory:
            val = val + self.inventory[item].xp_bonus
        xp_gain = val * opponent.xp
        self.xp = self.xp + xp_gain
        opponent.xp = 0
        print("\n%s's now has %i experiance points" % (self.name, self.xp))
        self.level_up()

class item:
    def __init__(self, name, type, attack, defense, luck, xp_bonus):
        self.name = name
        self.type = type
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.xp_bonus = xp_bonus

#Make a weapon subclass of Item



def battle(side_1, side_2, side_2_heals_at):
    defense_1 = side_1.defense_val()
    defense_2 = side_2.defense_val()
    go = True
    while go:
        status, defense = battle_turn(side_1, side_2, 0, defense_1, defense_2)
        if status == 'attack':
            defense_2 = defense
            if defense < 1:
                go = False
                loser = side_2
                winner = side_1
                break
        if status == 'heal':
            defense_1 = defense
        
        status, defense = battle_turn(side_2, side_1, 0, defense_2, defense_1)
        if status == 'attack':
            defense_1 = defense
            if defense < 1:
                go = False
                loser = side_1
                winner = side_2
                break
        if status == 'heal':
            defense_2 = defense
    write_string("\n%s has won!" % winner.name)
    winner.battle_xp(loser)
    winner.update_stats()
    loser.is_dead = True
    return winner

def battle_turn(active, idel, heal_at, defense_active, defense_idel):
    while active.is_player:
        write_string("What would you like to do? [Attack, Heal]:")
        choice = input(" ").lower()
        if choice == "attack":
            defense_idel = attack(active, idel, defense_idel)
            return 'attack', defense_idel
        elif choice == 'heal':
            defense_active = heal(active, defense_active)
            return 'heal', defense_active
        else:
            write_string("Please enter a valid input. ")
            continue
    if not active.is_player:
        if defense_active > heal_at:           
            defense_idel = attack(active, idel, defense_idel)
            return 'attack', defense_idel
        else:
            defense_active = heal(active, defense_active)
            return 'heal', defense_active


def attack(attack_side, defend_side, defense):
    flavor_text = [
        "\n%s's might strikes %s"
    ]
    flavor_text2 = [
        "%s's might was too much for %s to handle."
    ]
    write_string(random.choice(flavor_text) % (attack_side.name, defend_side.name))
    power = attack_side.attack_val()
    defense = defense - power
    write_string(" dealing %i damage. " % power)
    if defense < 1:
        write_string(random.choice(flavor_text2) % (attack_side.name, defend_side.name))
        write_string("\n%s has died.\n" % (defend_side.name))
        return 0
    else:
        write_string("%s's defensive strength is now: %i. \n" % (defend_side.name, defense))
    if attack_side.battle_luck() > defend_side.battle_luck():
        if attack_side.battle_luck() > defend_side.battle_luck():
                power = attack_side.attack_val()
                defense = defense - power
                write_string("Luckily enough, %s wins a bonus attack dealing %i damage " % (attack_side.name, power,))
                if defense < 1:
                    write_string(random.choice(flavor_text2) % (attack_side.name, defend_side.name))
                    write_string("\n%s has died." % (defend_side.name))
                    return 0
                else:
                    write_string("\n%s's defensive strength is now: %i" % (defend_side.name, defense))
    return defense

def heal(side, defense):
    heal_val = side.battle_luck() * side.health
    defense = defense + heal_val
    write_string("\n%s has healed %i. %s's defense is now %i" % (side.name, heal_val, side.name, defense))
    return defense


###Saves
class game:
    def __init__(self, save_name, story_point):
        self.save_name = save_name
        self.story_point = story_point
    def save(self):
        pass
    def load(self):
        pass

    def actions(actions): #for more then choices i.e.: viewing inventory, saving etc -- not actions
        write_string("The Jester apears sudently. The Jester gestures to a menu that you foolishly didn't notice before. [%s]:" % ", ".join(actions))
        action = input(' ')
        go = True
        while go:
            if action in actions:
                go = False
                excute(action)
            else:
                write_string("A jester in the making, choose form the list silly.")
    def excute(action):
        pass
        #save
        #save and exit
        #view inventory
        #read how game works
        #character info


def write_string(text):
    for line in text:
            for char in line:
                sleep(.06) #Should be .6 - Lowered for decoding
                sys.stdout.write(char)
                sys.stdout.flush()
def write_file(file_name):
    with open(file_name, 'r') as text:
        for line in text:
            for char in line:
                sleep(.06) #Should be .6 - Lowered for decoding
                sys.stdout.write(char)
                sys.stdout.flush()
    print(' ')
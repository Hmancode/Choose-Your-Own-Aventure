import story

def start():
    player = character('name', {}, 1, 1, 0, 5, 5, 0)
    items = define_items()
    characters = define_characters()
    story.game(player, characters, items, game)


def define_items():
    items = {
        "sword":item("Sword", 'weapon', 2, 4, 1, 1),
        "sheild":item("Sheild", 'weapon', 0, 10, 3, 2),
        "crystal":item("Crystal", 'artifact', 0, 0, 9, 5),
    }
    return items

def define_characters():
    characters = {
        "meanie":character("Meanie", {}, 20, 10, 3, 2,  999, 0),
    }
    return characters

class character:
    def __init__(self, name, inventory, strength, health, level, level_stats_base, max_items, xp):
        self.name = name
        self.inventory = inventory
        self.strength = strength
        self.health = health
        self.level = level
        self.level_stats_base = level_stats_base
        self.max_items = max_items
        self.xp = xp
    def is_dead(self):
        if self.health < 1:
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
        self.max_items = 5 + (self.level) * 1
        print("*Strength: %i --- Health: %i*" % (self.strength, self.health))
    def inventory_add(self, item):
        self.max_items = 1
        go = True
        while go:
            if len(self.inventory) > self.max_items:
                story.write_string("You cannot carry all that, you must remove somthing first.\n")
                self.inventory_edit()
                if len(self.inventory) > self.max_items:
                    con = input("Are you sure you do not want to continue without adding {}? [y/n]: ".format(item.name))
                    if con == 'y':
                        return
                    elif con == 'n':
                        pass
                    else:
                        story.write_string('Please input a vaild argument --- ')
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
                story.write_string('Please input a vaild argument --- ')
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
                    story.write_string('\nPlease input a vaild argument --- ')


class item:
    def __init__(self, name, type, attack, defense, luck, xp_bonus):
        self.name = name
        self.type = type
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.xp_bonus = xp_bonus

#Make a weapon subclass of Item


###Saves

class game:
    def __init__(self, save_name, story_point):
        self.save_name = save_name
        self.story_point = story_point
    def save(self):
        pass
    def load(self):
        pass

    def actions(actions): #for more thn choices i.e.: viewing inventory, saving etc -- not story actions
        story.write_string("The Jester apears sudently. The Jester foolishly gestures to a menu that you didn't notice before. [%s]:" % ", ".join(actions))
        action = input(' ')
        go = True
        while go:
            if action in actions:
                go = False
                excute(action)
            else:
                story.write_string("A jester in the making, choose form the list silly.")
    def excute(action):
        pass
        #save
        #save and exit
        #view inventory




start()
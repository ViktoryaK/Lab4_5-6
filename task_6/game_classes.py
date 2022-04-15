"""
Game classes
"""
import random

class Character:
    """
    character class
    """
    def __init__(self, name, description):
        self.description = description
        self.name = name
        self.power = None
        self.health = None
    def describe(self):
        print(f"You saw [{self.name}].")
        print(self.description)
    def set_power_health(self, power, health):
        self.power = power
        self.health = health

class MainCharacter(Character):
    """
    Main character
    """
    def __init__(self, name, description):
        super().__init__(name, description)
        self.health = 100
        self.power = 15
        self.defeated = 0
        self.mermaid = None

    def fight(self, enemy):
        helper = 0
        print(f"You chose to fight with {enemy.name}. Do you want to ask somebody's help?")
        answer = input("(y/n) ")
        if answer == "y":
            print("Who?")
            ans = input()
            if ans == enemy.help.name:
                print(f"{ans} came to help you.")
                helper = 50
            else:
                print(f"Unfortunately, {ans} is not a right choice.")
        else:
            print("It seems like you are going to fight alone.")
        print(f"Your enemy has health:{enemy.health}")
        if helper:
            print(f"{enemy.help.name} attacked first. Attack was extremely powerful.")
            enemy.health -= helper
            print("You have to finish by yourself")
        while self.health > 0 and enemy.health > 0:
            print(f"Enemy's health: {enemy.health}, Your health: {self.health}")
            print("You attacked.")
            en_action = random.choice(['dodge', 'suffer'])
            if en_action == 'dodge':
                print("The enemy dodged.")
            else:
                enemy.health -= self.power
                print("The enemy failed in dodging")
            print("Enemy attacked. You are trying to dodge.")
            action = random.choice(['dodge', 'suffer'])
            if action == 'dodge':
                print("You dodged.")
            else:
                print("You failed in dodging")
                self.health -= enemy.power
        if self.health <= 0:
            return False
        elif enemy.health <= 0:
            return True

    def fight_boss(self, backpack, strength):
        print("The evil boss is right before your eyes. His health is enormous. And his power is too big for you. Unless you think. Just a bit")
        if backpack:
            print("Do you want to use one of the items you have in your backpack?")
            answ = input("(y/n) ")
            if answ == 'y':
                print(" ".join([obj.name for obj in backpack]))
                print("Which one?")
                this = input()
            else:
                print("You decided to fight only with your own powers and... you lost... You are dead.")
                return False
            if this == strength.name:
                print(
                    "You did it! The rune of strength helped you and with one powerful sword thrust you killed the main enemy!")
                print("Congratulations, you have vanquished all the enemies!")
                return True
            else:
                print("Unfortunately, it didn't help. Koschei wasn't damaged enough by your attack and he hit back. You died from his single punch.")
                return False

class Enemy(Character):
    """
    Enemy
    """
    def __init__(self, name, description):
        super().__init__(name, description)
        self.help = None
    def set_helper(self, helper):
        self.help = helper
    def talk(self):
        return f"This creature doesn`t seem to want to talk. If you don't want to be killed, it would be better not to talk to {self.name}."

class Boss(Enemy):
    """
    Boss
    """
    def fight(self, fight_with):
        pass
    def talk(self):
        return "Talking to that evil creature is pointless if you want to live."


class Ally(Character):
    """
    Ally
    """
    def __init__(self, name, describe):
        super().__init__(name, describe)
        self.help_phrase = ""

    def talk(self, player):
        print("""
-Hi, nice to meet you. I'm here to fight the enemies and I really need some help. - You said.
Choose (number) what do you want to say:
1. How can you help me?
2. Do you know who the bad guys are?
""")
        if self.name == "Perelesnyk" and player.mermaid == True:
            print("""
3. Mermaid asked to give you something.""")
        number = int(input("> "))
        if number == 1:
            if self.name == "Perelesnyk":
                print(self.help_phrase)
            else:
                print(self.help_phrase)
        elif number == 2:
            print("-It's obvious. There are Babay, Baba Yaga, Zmiy Gorynych and Koshcei the Deathless in our city.")
        elif number == 3 and player.mermaid == True and self.name == "Perelesnyk":
            player.mermaid = "done"
            print("Oh, I see. - He smiled. - Thank you.")
        else:
            print('Please, enter number')
        if self.name == "Perelesnyk":
            print("Do you want to receive new sword?")
            answ = input("(y/n) ")
            if answ == 'y':
                print("Perelesnyk smirked and started working. He finished soon and your new sabre significantly raised your power.")
                player.power += 30
                print(player.power)
            else:
                if player.mermaid == 'needle' and player.defeated == 3:
                    print("-So what do you want?")
                    print("Destroy it. - You showed him a needle.")
                    print("Perelesnyk laughed and accepted your request. He took the needle with death of the Deathless in it and burned it to ashes!")
                    print("All the enemies died. And you won.")


    def set_help_phrase(self, help_phrase):
        self.help_phrase = help_phrase

class Informer(Character):
    """
    Informer
    """
    def talk(self, player):
        print("""
-Hi, nice to meet you. I'm here to fight the enemies and I really need some help. - You said. 
-How can you help me?""")
        print("I don't answer questions. I ask question. Answer my riddle or die.")
        answer = input("Do you wanna answer the riddle or run away?(y/n) ")
        if answer == "n":
            return "So go away."
        elif answer == "y":
            print("What creature walks on four legs in the morning, two legs in the afternoon, and three legs in the evening?")
            answer1 = input().lower()
            if answer1 == "human":
                return """Sphinx glazed at you.
-That's right.
-Now you can answer my question?
-Since the pure human like you don't know what he wants to know. - He completely ignored you. - I will give you a hint.
The Sphinx moved his enormous wings and majestically said:
    "On the sea or in the ocean there is an island, 
    on that island stands an oak,
    under the oak there is a box, 
    in the box there is a bunny, 
    in the bunny there is a goose,
    in a goose - an egg, 
    in an egg - a needle, 
    and in a needle - death of the Deathless»
    However, - added Sphinx in the end, - some fairy tales claim that Chahlik can be killed with one strong hit...

"""

class Item:
    """
    Item
    """
    def __init__(self, name):
        self.name = name
    def describe(self):
        print(f"You saw [{self.name}].")

class Runes(Item):
    """
    Runes
    """
    def __init__(self, name):
        super().__init__(name)


class DeathItems(Item):
    """
    Bring death
    """
    def __init__(self, name, death):
        super().__init__(name)
        self.death = death


class Room:
    """
    Room
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.character = []
        self.item = None
        self.rooms = []

    def get_details(self):
        print(f"We arrived at the {self.name}.")
        print(self.description)
        for room in self.rooms:
            if self.name != room[0].name:
                print(f"The {room[0].name} is {room[1]}")

    def link_room(self, room, way):
        self.rooms.append([room, way])

    def move(self, command):
        for room in self.rooms:
            if room[1] == command:
                if room[0].name != self.name:
                    return room[0]
                else:
                    print("There are nowhere to go.")
                    return room[0]

    def set_character(self, character):
        self.character.append(character)
    def set_item(self, item):
        self.item = item
    def get_character(self):
        return self.character
    def get_item(self):
        return self.item
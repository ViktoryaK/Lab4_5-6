class Room:
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.character = None
        self.item = None
        self.rooms = []
    def get_details(self):
        print(self.name)
        print('--------------------')
        print(self.description)
        for room in self.rooms:
            print(f"The {room[0].name} is {room[1]}")
    def move(self, command):
        for room in self.rooms:
            if room[1] == command:
                return room[0]
    def set_description(self, description):
        self.description = description
    def link_room(self, room, way):
        self.rooms.append([room, way])
    def set_character(self, character):
        self.character = character
    def set_item(self, item):
        self.item = item
    def get_character(self):
        return self.character
    def get_item(self):
        return self.item
class Enemy:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.phrase = ""
        self.weakness = ""
    def set_conversation(self, phrase):
        self.phrase = phrase
    def set_weakness(self, weakness):
        self.weakness = weakness
    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)
    def talk(self):
        print(f"[{self.name} says]: {self.phrase}")
    def fight(self, fight_with):
        if self.weakness == fight_with:
            return True
        return False
    def get_defeated(self, x=0):
        x+=1
        return x
class Item:
    def __init__(self, name):
        self.name = name
        self.description = ""
    def set_description(self, description):
        self.description = description
    def describe(self):
        print(f"The [{self.name}] is here - {self.description}")
    def get_name(self):
        return self.name

# єдина проблема полягає в тому, як блін зробити get_defeated правильно
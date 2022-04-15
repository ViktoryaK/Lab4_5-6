import game_classes

chicken_leg_house = game_classes.Room("Chicken Leg House", "It is a frightening house in the woods where someone lives.")
snake_cave = game_classes.Room("Snake Cave", "That's an enormous cave with many treasures")
city_zoo = game_classes.Room("City Zoo", "It's a small desert made just for one special guest.")
northern_forest = game_classes.Room("Northern forest", "It's the place where Mavka lives.")
lake_of_mermaids = game_classes.Room("Lake of mermaids", "It is the home of Mermaid")
smithy = game_classes.Room("Smithy", "Here the blacksmith Perelesnyk works with all kinds of weapons and metal")
city_gate = game_classes.Room("City gate", "Now we are right at the entrance of the city")
dark_castle = game_classes.Room("Dark castle", "This is the home of the last boss")

chicken_leg_house.link_room(northern_forest, "south")
chicken_leg_house.link_room(chicken_leg_house, "north")
chicken_leg_house.link_room(chicken_leg_house, "east")
chicken_leg_house.link_room(chicken_leg_house, 'west')
snake_cave.link_room(northern_forest, "east")
snake_cave.link_room(snake_cave, "west")
snake_cave.link_room(snake_cave, "north")
snake_cave.link_room(snake_cave, "south")
city_zoo.link_room(city_gate, "east")
city_zoo.link_room(city_zoo, "west")
city_zoo.link_room(city_zoo, "north")
city_zoo.link_room(city_zoo, "south")
northern_forest.link_room(city_gate, "south")
northern_forest.link_room(chicken_leg_house, "north")
northern_forest.link_room(snake_cave, "west")
northern_forest.link_room(dark_castle, "east")
lake_of_mermaids.link_room(city_gate, "west")
lake_of_mermaids.link_room(lake_of_mermaids, "east")
lake_of_mermaids.link_room(lake_of_mermaids, "north")
lake_of_mermaids.link_room(lake_of_mermaids, "south")
smithy.link_room(city_gate, "north")
smithy.link_room(smithy, "west")
smithy.link_room(smithy, "east")
smithy.link_room(smithy, "south")
city_gate.link_room(smithy, "south")
city_gate.link_room(city_zoo, "west")
city_gate.link_room(lake_of_mermaids, "east")
city_gate.link_room(northern_forest, "north")
dark_castle.link_room(northern_forest, "west")
dark_castle.link_room(dark_castle, "east")
dark_castle.link_room(dark_castle, "north")
dark_castle.link_room(dark_castle, "south")

babay = game_classes.Enemy("Babay", "He was a pitch-black and crooked old man hiding behind the trees.")
yaga = game_classes.Enemy("Baba Yaga", "She was a deformed and ferocious-looking woman with a big crooked nose and evilish eyes.")
zmiy = game_classes.Enemy("Zmiy Gorynych", "A large dragon with three heads was peacefully sleeping.")
koschei = game_classes.Boss("Koshcei the Deathless", "An evil super dangerous skeleton was looking straight at you.")
perelesnyk = game_classes.Ally("Perelesnyk", "A handsome boy was observing the red-hot sword in his hands with a smile.")
mermaid = game_classes.Ally("Mermaid", "The beautiful girl with blue hair was staring at you from the water.")
mavka = game_classes.Ally("Mavka", "This creature was sitting on the ground and carefully observing the babay. She was paying no attention to you.")
chugajstr = game_classes.Ally("Chugajstr", "An old man with pure white hair and beard was sitting on the ground.")
sphinx = game_classes.Informer("Sphinx", "There was a friendly, but dangerous creature, a winged monster having a woman's head and a lion's body.")
player = game_classes.MainCharacter("Kozak", "Player")


babay.set_power_health(20, 80)
yaga.set_power_health(15, 100)
zmiy.set_power_health(20, 100)
player.set_power_health(15, 300)

babay.set_helper(mavka)
yaga.set_helper(chugajstr)

perelesnyk.set_help_phrase("Well, since I am working here, it's obvious that I can make you a sword. Just ask))")
chugajstr.set_help_phrase("I am just sitting here, traveller, so, if you not wanna kill Mavka, there is nothing I can help you with. Oh, except hunting that Baba. Don't like her.")
mavka.set_help_phrase("Well, that Babay is pissing me off even more than Chugajstr, so, if you ask, I can help to defeat him.")
mermaid.set_help_phrase("""Well... I can help you with... something)) 
You will know what can be hidden in water, if you talk to Sphinx. 
But to receive my help, you have to help me first. Here, give this to Perelesnyk and go back.""")



defence = game_classes.Runes("Rune Oud")
health = game_classes.Runes("Rune Krada")
strength = game_classes.Runes("Rune Strength")
apples = game_classes.DeathItems("Youth-giving apples", "You dared to pick up favorite apples of Zmiy! You were killed!")
water = game_classes.DeathItems("Living and dead water", "You dared to pick up the property of the Deathless. He killed you for what you did.")
mortar = game_classes.DeathItems("Jaga's mortar", "You laid your hand on something that isn't yours and you will pay.")
chest = game_classes.Item("Wooden chest")

chicken_leg_house.set_character(yaga)
snake_cave.set_character(zmiy)
northern_forest.set_character(babay)
dark_castle.set_character(koschei)
smithy.set_character(perelesnyk)
lake_of_mermaids.set_character(mermaid)
northern_forest.set_character(mavka)
city_gate.set_character(chugajstr)
city_zoo.set_character(sphinx)

snake_cave.set_item(strength)
lake_of_mermaids.set_item(chest)
city_zoo.set_item(defence)
smithy.set_item(mortar)
northern_forest.set_item(apples)
chicken_leg_house.set_item(water)
dark_castle.set_item(health)


current_room = city_gate
backpack = []

dead = False


try:
    while not dead:
        print("\n")
        print("Actions: talk, take, fight, north, south, east, west")
        current_room.get_details()
        inhabitants = current_room.get_character()
        if inhabitants is not None:
            for inhabitant in inhabitants:
                inhabitant.describe()

        item = current_room.get_item()
        if item is not None:
            item.describe()

        command = input("> ")

        if command in ["north", "south", "east", "west"]:
            # Move in the given direction
            current_room = current_room.move(command)
        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            if inhabitants is not None:
                print("Who do you want to talk to?")
                name = input("> ")
                for inhabitant in inhabitants:
                    if inhabitant.name == name:
                        if name == 'Mermaid' and player.mermaid == 'done':
                            print("""-Oh, you're back. Thanks a lot. Now, about your problem. I will help you open a [Wooden chest].
She found the key and opened a chest in which was... a bunny? She was doing something magical over and over and soon after goose, and egg she got a needle!
-Remember, only fire can destroy it. Now, go away, go.""")
                            player.mermaid = 'needle'
                        else:
                            inhabitant.talk(player)
                            if inhabitant.talk(player) == "The end":
                                dead = True
                            if name == 'Mermaid':
                                player.mermaid = True
                    else:
                        print("Incorrect name")
            else:
                print("There is no one here to talk to!")
        elif command == "fight":
            if inhabitants is not None:
                print("Who will you fight with?")
                fight_with = input()
                for inhabitant in inhabitants:
                    if inhabitant.name == fight_with:
                        if isinstance(inhabitant, game_classes.Ally) or isinstance(inhabitant, game_classes.Informer):
                            print(f"You don't have to fight with a {fight_with}. It`s not an enemy!")
                        elif isinstance(inhabitant, game_classes.Boss):
                            if player.defeated == 3:
                                result = player.fight_boss(backpack, strength)
                                if result:
                                    current_room.character = None
                                    dead = True
                                else:
                                    dead = True
                            else:
                                print("You cannot fight the Final Boss without defeating all the other enemies.")
                        else:
                            result = player.fight(inhabitant)
                            if result:
                                current_room.character = None
                                player.defeated += 1
                            else:
                                dead = True
            else:
                print("There is no one here to fight with")
        elif command == "take":
            if item:
                if isinstance(item, game_classes.DeathItems):
                    print(item.death)
                    dead = True
                print("You put the " + item.name + " in your backpack")
                backpack.append(item)
                current_room.set_item(None)
            else:
                print("There's nothing here to take!")
        else:
            print("I don't know how to " + command)
    print("The end")
except:
    print("Incorrect input")
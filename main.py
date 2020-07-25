import random as rd

player_name = input("Enter your name\n")
valid = True


class Player:
    def __init__(self, name, health, attack, super_attack, super_attack_num, defense, healing_potions):
        self.name = name
        self.health = health
        self.attack = attack
        self.super_attack = super_attack
        self.super_attack_num = super_attack_num
        self.defense = defense
        self.healing_potions = healing_potions

    def attack_monster(self, monster):
        global valid
        damage = self.attack - monster.defense
        damage += rd.randint(-10, 10)
        monster.health -= damage
        if monster.health < 0:
            monster.health = 0
        print("{} attacks the monster dealing {} damage".format(player_.name, damage))
        print("Monster has now {} health".format(monster.health))
        valid = True

    def super_attack_monster(self, monster):
        global valid
        if self.super_attack_num > 0:
            damage = self.super_attack - monster.defense
            damage += rd.randint(-20, 20)
            monster.health -= damage
            self.super_attack_num -= 1
            if monster.health < 0:
                monster.health = 0
            print("{} super attacks the monster dealing {} damage".format(player_name, damage))
            print("Monster now has {} health".format(monster.health))
            valid = True
        else:
            print("You ran out of super attacks")
            valid = False

    def heal(self):
        global valid
        if self.health != 1000:
            if self.healing_potions > 0:
                self.health += 100
                self.healing_potions -= 1
                if self.health > 1000:
                    self.health = 1000
                print("{} healed for 100 health points".format(player_.name))
                print("{} now has {} health".format(player_.name, player_.health))
                valid = True
            else:
                print("You ran out of healing potions")
                valid = False
        else:
            print("You already have full health")
            valid = False


class Monster:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_player(self, player):
        damage = self.attack - player.defense
        damage += rd.randint(-10, 10)
        player.health -= damage
        if player.health < 0:
            player.health = 0
        print("Monster attacks {} dealing {} damage".format(player_.name, damage))
        print("You now have {} health points".format(player_.health))



player_ = Player(player_name, 1000, 50, 80, 6, 10, 4)
monster_ = Monster(500, 40, 5)
large_monster_ = Monster(800, 60, 10)

print("""
Your states:

Health: {}
Attack Damage: {}
Super Attack Damage: {}
Number of Super Attacks: {}
Defense: {}
Healing Potions: {}
""".format(player_.health, player_.attack, player_.super_attack, player_.super_attack_num,
           player_.defense, player_.healing_potions))

print()
input("Press Enter to start the game")
print()
print("A monster has appeared!")
print()
print("""
Monster States:
Health: {}
Attack Damage: {}
Defense: {}
""".format(monster_.health, monster_.attack, monster_.defense))
print()
print()

while True:
    print()
    print("Your turn!")
    print("Choose your action!")
    print("""
    1- Attack
    2- Super Attack ({} Super Attacks left)
    3- Heal ({} Healing Potions left)
    """.format(
        player_.super_attack_num,
        player_.healing_potions
    ))
    print()
    action = input("Your action: ")

    if action == "1":
        player_.attack_monster(monster_)
        if monster_.health == 0:
            print("{} defeated the monster!".format(player_.name))
            break

    elif action == "2":
        player_.super_attack_monster(monster_)
        if monster_.health == 0:
            print("{} defeated the monster!".format(player_.name))
            break

    elif action == "3":
        player_.heal()

    else:
        print("Choose a valid number")
        continue

    if not valid:
        continue

    print()
    print("Monster's turn!")
    print()
    monster_.attack_player(player_)
    if player_.health == 0:
        print("You lost the game")
        input()
        exit()


print()
print("A large Monster has appeared")
print()

while True:
    print()
    print("Your turn!")
    print("Choose your action!")
    print("""
    1- Attack
    2- Super Attack ({} Super Attacks left)
    3- Heal ({} Healing Potions left)
    """.format(
        player_.super_attack_num,
        player_.healing_potions
    ))
    print()
    action = input("Your action: ")

    if action == "1":
        player_.attack_monster(large_monster_)
        if large_monster_.health == 0:
            print("{} defeated the large monster!".format(player_.name))
            break

    elif action == "2":
        player_.super_attack_monster(large_monster_)
        if large_monster_.health == 0:
            print("{} defeated the large monster!".format(player_.name))
            break

    elif action == "3":
        player_.heal()

    else:
        print("Choose a valid number")
        continue

    if not valid:
        continue

    print()
    print("Monster's turn!")
    print()
    large_monster_.attack_player(player_)
    if player_.health == 0:
        print("You lost the game")
        break

input()


import random

class Character:
    def __init__(self, name, health, attack_power, defense_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self, target):
        damage = self.attack_power - target.defense_power
        target.health -= damage
        print(f"{self.name} attacks {target.name} and deals {damage} damage.")

    def defend(self, damage):
        self.health -= damage
        print(f"{self.name} defends and takes {damage} damage.")

    def is_alive(self):
        return self.health > 0

# Create two characters
player_name = input("Enter your character's name: ")
player_health = int(input("Enter your character's health: "))
player_attack_power = int(input("Enter your character's attack power: "))
player_defense_power = int(input("Enter your character's defense power: "))
player = Character(player_name, player_health, player_attack_power, player_defense_power)

enemy_name = input("Enter the enemy's name: ")
enemy_health = int(input("Enter the enemy's health: "))
enemy_attack_power = int(input("Enter the enemy's attack power: "))
enemy_defense_power = int(input("Enter the enemy's defense power: "))
enemy = Character(enemy_name, enemy_health, enemy_attack_power, enemy_defense_power)

# Simulate combat
while player.is_alive() and enemy.is_alive():
    attacker = random.choice([player, enemy])
    defender = enemy if attacker == player else player

    if attacker == player:
        attacker.attack(defender)
    else:
        damage = random.randint(5, 15)
        attacker.attack(defender)
        defender.defend(damage)

# Determine the winner
if player.is_alive():
    print("Player wins!")
else:
    print("Enemy wins!")
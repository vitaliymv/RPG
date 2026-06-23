# pip install streamlit
import random


class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class

        self.level = 1
        self.exp = 0
        self.gold = 100
        self.max_hp = 100
        self.hp = 100
        self.strength = 10
        self.defense = 5
        self.inventory = []

    def fight(self):
        monsters = [
            ("Goblin", 20, 30),
            ("Skelet", 30, 50),
            ("Orc", 50, 80)
        ]
        monster, gold_reward, exp_reward = random.choice(monsters)
        damage = random.randint(
            5, exp_reward / 2
        )
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 1
            self.exp -= exp_reward
        else:
            self.gold += gold_reward
            self.exp += exp_reward
        self.check_level()
        return monster, damage, gold_reward, exp_reward

    def check_level(self):
        while self.exp >= self.level * 100:
            self.level += 1
            remaining_exp = self.exp - self.level * 100
            self.exp = remaining_exp
            self.max_hp += 20
            self.hp = self.max_hp
            self.strength += 2
            self.defense += 2

    def heal(self):
        if self.gold >= 20:
            if self.hp < self.max_hp:
                self.gold -= 20
                self.hp = self.max_hp
            return True
        return False

    def train(self):
        self.strength += 1
        self.defense += 1

    def cast_spell(self):
        damage = random.randint(10, 40)
        return damage

    def add_item(self, item):
        self.inventory.append(item)

    def to_dict(self):
        return {
            "name": self.name,
            "hero_class": self.hero_class,
            "level": self.level,
            "exp": self.exp,
            "gold": self.gold,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "strength": self.strength,
            "defense": self.defense,
            "inventory": self.inventory,
        }

    @staticmethod
    def from_dict(cls, data):
        hero = cls(data["name"], data["hero_class"])
        hero.level = data["level"]
        hero.exp = data["exp"]
        hero.gold = data["gold"]
        hero.hp = data["hp"]
        hero.max_hp = data["max_hp"]
        hero.strength = data["strength"]
        hero.defense = data["defense"]
        hero.inventory = data["inventory"]
        return hero
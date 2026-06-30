# pip install streamlit
import random


class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class

        self.level = 1
        self.exp = 0
        self.gold = 100
        self.strength = 10
        self.max_hp = 100 + self.strength
        self.hp = 110
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
            5, int(exp_reward / 3) * self.level
        )
        damage -= self.defense
        self.hp -= damage
        rand_gold = 0
        if self.hp <= 0:
            self.hp = 1
            self.exp -= exp_reward
        else:
            rand_gold = random.randint(gold_reward, gold_reward * self.level)
            self.gold += rand_gold
            self.exp += exp_reward
        self.check_level()
        return monster, damage, rand_gold, exp_reward

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
        if self.gold >= self.max_hp // 2:
            if self.hp < self.max_hp:
                self.gold -= self.max_hp // 2
                self.hp = self.max_hp
            return True
        return False

    def train(self):
        if self.gold >= 90:
            self.gold -= 90
            self.strength += 1
            self.defense += 1
            return True
        else:
            return False

    def add_item(self, item, product):
        if "strength" in product:
            self.strength += product["strength"]
        if "defense" in product:
            self.defense += product["defense"]

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
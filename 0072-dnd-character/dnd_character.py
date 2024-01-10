import random


def modifier(score):
    return (score - 10) // 2


class Character:
    def __init__(self):
        self.abilities = [self.generate_ability() for _ in range(6)]
        (
            self.strength, self.dexterity, self.constitution, self.intelligence,
            self.wisdom, self.charisma
        ) = self.abilities
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def generate_ability():
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        dice_rolls.remove(min(dice_rolls))
        return sum(dice_rolls)

    def ability(self):
        return random.choice(self.abilities)

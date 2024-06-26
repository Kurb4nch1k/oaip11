from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    @abstractmethod
    def attack(self):
        pass

class MeleeWeapon(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self, target):
        return f"Attacking {target} with {self.name} for {self.damage} damage!"

class RangedWeapon(Weapon):
    def __init__(self, name, damage, range):
        super().__init__(name, damage)
        self.range = range

    def attack(self, target):
        return f"Shooting {target} with {self.name} for {self.damage} damage at a range of {self.range}!"

class Sword(MeleeWeapon):
    def __init__(self):
        super().__init__("Sword", 10)

class Axe(MeleeWeapon):
    def __init__(self):
        super().__init__("Axe", 12)

class Gun(RangedWeapon):
    def __init__(self):
        super().__init__("Gun", 15, 50)

class Bow(RangedWeapon):
    def __init__(self):
        super().__init__("Bow", 10, 100)

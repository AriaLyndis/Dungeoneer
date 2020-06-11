class Monster:
    def __init__(self, name, armor, damage, accuracy, hp):
        self.armor = armor
        self.damage = damage
        self.accuracy = accuracy
        self.hp = hp


# Level 1
Skeleton = Monster("Skeleton", 10, 3, 3, 5)
GiantRat = Monster("Giant Rat", 11, 5, 3, 10)

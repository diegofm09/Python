
class Goblin:

    def attack(self):
        pass


class Dragon:

    def attack(self):
        pass


class EnemyFactory:
    
    @staticmethod
    def create_enemy(difficulty):
        if difficulty == "easy":
            return Goblin()
        elif difficulty == "hard":
            return Dragon()
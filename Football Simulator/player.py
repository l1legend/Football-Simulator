import random


class Players:
    """
    player is on a single team, with many other players
    players play in a game for a team
    """

    def __init__(self, name, skill):
        self.name = name

        # player skill rankings
        self.skill = skill

    def salary(self):
        return 5000 + self.skill * 100

    def __str__(self):
        return '{}, Skill: {}, Salary {}'.format(
            self.name, self.skill, self.salary())


def generate_player():
    first_names = [
        'Sophia', 'Jackson', 'Emma', 'Aiden', 'Olivia', 'Lucas', 'Ava', 'Liam', 'Mia', 'Noah', 'Isabella', 'Ethan',
        'Riley', 'Mason', 'Aria', 'Caden', 'Zoe', 'Oliver', 'Charlotte', 'Elijah', 'Lily', 'Grayson', 'Layla', 'Jacob',
        'Amelia', 'Michael', 'Emily', 'Benjamin', 'Madelyn', 'Carter', 'Aubrey', 'James', 'Adalyn', 'Jayden',
        'Madison', 'Logan', 'Chloe', 'Alexander',
    ]
    first_name = random.choice(first_names)
    last_name = random.choice(first_names)

    full_name = '{} {}'.format(first_name, last_name)
    # generate skill and salary
    skill = 10 + random.randint(0, 90)
    return Players(full_name, skill)

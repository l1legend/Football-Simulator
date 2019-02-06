import copy
import random


class Team:
    """
    Team has many players
    Team has a ranking in a league
    Team plays games against other teams
    Team has a single manager
    """

    def __init__(self, name):
        self.name = name
        self.players = []

        self.wins = 0
        self.losses = 0

        self.money = 1000000


    def weekly_salary(self):
        salary = 0
        for player in self.players:
            salary += player.salary()
        return salary

    def pay_players(self):
        self.money -= self.weekly_salary()

    def rating(self):
        """
        what is the rating of the team
        """
        rating = 0
        for player in self.players:
            rating += player.skill

        return rating

    def __str__(self):
        return '{} {}'.format(self.name, self.rating())


class Game:
    """
    plays a game between two teams
    game belongs to a league
    """

    def __init__(self, league, home_team, away_team):
        self.league = league
        self.home_team = home_team
        self.away_team = away_team

        self.home_team_won = None

        print('{}  vs. {}'.format(self.home_team, self.away_team))

    def play(self):
        """
        play the game, return who won
        True means the home team won, False means the away team won
        """
        print('Play begins')
        # insert game here

        print('Play ends')
        if self.home_team.rating() > self.away_team.rating():
            print('{} wins'.format(self.home_team))
            self.home_team_won = True
        else:
            print('{} wins.'.format(self.away_team))
            self.home_team_won = False


class League:
    """
    league has many teams
    each team is going to have a ranking within this league
    """

    def __init__(self, name, teams, players):
        self.name = name
        self.teams = teams
        self.players = players
        self.rounds_played = 0

    def play_round(self):
        """
        play a round, which is 3 games
        """
        print('Round begins')
        num_teams = len(self.teams)
        num_games = num_teams // 2

        teams_to_play = copy.copy(self.teams)

        for game_num in range(num_games):
            home_team = random.choice(teams_to_play)
            teams_to_play.remove(home_team)
            away_team = random.choice(teams_to_play)
            teams_to_play.remove(away_team)

            game = Game(self, home_team, away_team)
            game.play()
            self.resolve_game(game)

        print('Round ends')
        self.rounds_played += 1

        # ladder status
        self.ladder()

    def ladder(self):
        for team in sorted(self.teams, key=lambda t: -t.wins):  # sorted function copies list and sorts it '-' sorts team with most wins to top
            print('{} {} wins'.format(team, team.wins))

    def resolve_game(self, game):
        if game.home_team_won:
            # home team won
            game.home_team.wins += 1
            game.away_team.losses += 1
            game.home_team.money += round(200000*random.random())

        else:
            # away team won
            game.away_team.wins += 1
            game.home_team.losses += 1
            game.away_team.money += round(200000*random.random())

        game.home_team.pay_players()
        game.away_team.pay_players()

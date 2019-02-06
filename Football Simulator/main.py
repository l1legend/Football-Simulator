import random
from teammanager import TeamManager
from player import generate_player
from team import League, Team



def main():
    # set up our data
    # generate some players
    players = []
    for i in range(100):
        players.append(generate_player())

    # set up 6 teams
    teams = [
        Team('Chelsea'),
        Team('Man City'),
        Team('Arsenal'),
        Team('West Ham'),
        Team('Hull City'),
        Team('Swansea'),
    ]

    for team in teams:
        for player_num in range(11):
            # give them 11 starting players
            selected_player = random.choice(players)
            team.players.append(selected_player)
            players.remove(selected_player)

    # we have a single league
    first_league = League('Premiership League', teams, players)

    # create the manager
    manager = TeamManager(random.choice(teams), first_league)

    print('Season begins')
    for i in range(10):
        manager.manage()
        first_league.play_round()
    print('Season ends')


if __name__ == '__main__':
    main()

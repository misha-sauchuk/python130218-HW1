"""Реализовать систему хранения информации о футбольном чемпионате. Информация опирается на следующие основные классы:
Team (команда), Player (игрок), Match (матч). Эти классы связаны друг с другом посредством ассоциации.

Реализовать возможность сохранения записей в файл, а также возможность поиска информации о матчах в указанные даты
(предусмотреть возможность поиска по временному периоду) с выводом информации по командам и игрокам,
участвовавшим в матчах.
"""
import json



class Players:
    def __init__(self, player):  # player - dict with info about one player (one line in file players)
        self.id_player = player.get('id_player') + '_pl'
        self.name = player.get('name')
        self.team = player.get('team')

    def __str__(self):
        return '{} plays in {}'.format(self.name, self.team)


class Teams:
    def __init__(self, team):  # team - dict with info about one team (one line in file teams)
        self.id_team = team.get('id_team') + '_team'
        self.name = team.get('name')
        self.players_in_team()

    # function to find players in this team
    def players_in_team(self):
        self.players_in_team = []
        if players_ins:
            for player in players_ins:
                if player.team == self.name:
                    self.players_in_team.append(player.name)


# function to open files and take data
def load_data(file_name):
    data_list = []
    with open(file_name) as file:
        for line in file:
            data_list.append(json.loads(line))
        return data_list


players_file = 'players.json'  # file name with players information
players_list = load_data(players_file)  # data from file -> is in list, each elements is dict
players_ins = []  # list to put here a instance of the class Players
for player in players_list:  # circle to create instance and put it to the list
    player = Players(player)
    players_ins.append(player)

teams_file = 'teams.json'  # file name with teams information
teams_list = load_data(teams_file)  # data from file -> is in list, each elements is dict
teams_ins = []  # list to put here a instance of the class Teams
for team in teams_list:  # circle to create instance and put it to the list
    team = Teams(team)
    teams_ins.append(team)


# test to the task
if __name__ == '__main__':
    for i in range(len(players_ins)):
        print(players_ins[i])
    print(teams_ins[0].players_in_team)

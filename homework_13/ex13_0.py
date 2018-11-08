"""Реализовать систему хранения информации о футбольном чемпионате. Информация опирается на следующие основные классы:
Team (команда), Player (игрок), Match (матч). Эти классы связаны друг с другом посредством ассоциации.

Реализовать возможность сохранения записей в файл, а также возможность поиска информации о матчах в указанные даты
(предусмотреть возможность поиска по временному периоду) с выводом информации по командам и игрокам,
участвовавшим в матчах.
"""
import json
import datetime


class Players:
    def __init__(self, player):  # player - dict with info about one player (one line in file players)
        self.id_player = player.get('id_player') + '_pl'
        self.name = player.get('name')
        self.team = player.get('team')


class Teams:
    def __init__(self, team):  # team - dict with info about one team (one line in file teams)
        self.id_team = team.get('id_team') + '_team'
        self.name = team.get('name')
        self.players_in_team(self)

    # function to find players in this team
    @staticmethod
    def players_in_team(self):
        self.players_in_team = []
        if players_ins:
            for player in players_ins:
                if player.team == self.name:
                    self.players_in_team.append(player.name)


class Match:
    def __init__(self, match):
        self.id_match = match.get('id_match') + '_match'
        self.date = datetime.datetime.strptime(match.get('date'), '%d/%m/%Y')
        self.location = match.get('location')
        self.result = match.get('result')
        self.team1 = match.get('team1')
        self.team2 = match.get('team2')
        self.players_in_match(self)

    @staticmethod
    def players_in_match(self):
        self.players_in_match = []
        if players_ins:
            for player in players_ins:
                if player.team == self.team1 or player.team == self.team2:
                    self.players_in_match.append(player.name)

    def __str__(self):
        return '{} and {} played {} in the {}'.format(self.team1, self.team2, self.date, self.location)


# function to open files and take data
def load_data(file_name):
    data_list = []
    with open(file_name) as file:
        for line in file:
            data_list.append(json.loads(line))
        return data_list


# function to create instances
def create_instance(file_name):
    instance_list = load_data(file_name)  # data from file -> is in list, each elements is a dict
    instance = []  # list to put here an instance of the class
    for item in instance_list:  # circle to create instance and put it into the list
        if file_name.startswith('player'):
            item = Players(item)
        elif file_name.startswith('team'):
            item = Teams(item)
        elif file_name.startswith('match'):
            item = Match(item)
        instance.append(item)
    return instance


players_file = 'players.json'  # file name with players information
players_ins = create_instance(players_file)

teams_file = 'teams.json'  # file name with teams information
teams_ins = create_instance(teams_file)

match_file = 'match.json'  # file name with matc information
match_ins = create_instance(match_file)


# function to check the wright input format of the date
def date_format(date):
    try:
        date = datetime.datetime.strptime(date, '%d/%m/%Y')
        return date
    except ValueError as er:
        print(er.__class__.__name__, er)


# function to search march info at the day
def search_in_day():
    date = input('Please, enter date you would like to check (dd.mm.yyyy): ')
    date = date_format(date)
    for instance in match_ins:
        if instance.date == date:
            print(instance)
            to_do = input('Do you want to see players of this match Y/N: ')
            if to_do.upper() == 'YES' or to_do.upper() == 'Y':
                print(instance.players_in_match)


# function to search march info during the period
def search_during_period():
    date1 = input('Please, enter date you would like to start to check (dd.mm.yyyy): ')
    date1 = date_format(date1)
    date2 = input('Please, enter date you would like to stop to check (dd.mm.yyyy): ')
    date2 = date_format(date2)
    for instance in match_ins:
        if date1 <= instance.date <= date2:
            print(instance)
            to_do = input('Do you want to see players of this match Y/N: ')
            if to_do.upper() == 'YES' or to_do.upper() == 'Y':
                print(instance.players_in_match)


# test to the task
if __name__ == '__main__':
    print(teams_ins[0].players_in_team)
    print(match_ins[0].players_in_match)
    print(match_ins[1].location)
    while True:
        to_search = input('Please, enter do you want to search at the day(1) on in period(2) or exit(3): ')
        if to_search == '1':
            search_in_day()
        elif to_search == '2':
            search_during_period()
        elif to_search == '3':
            break
"""Реализовать класс лифта Elevator. Класс должен обладать методом, lift, отвечающий за вызов лифта.
При сложении/вычитании экземпляров класса должно возвращаться значение производимой математической операции.
Если производить вычитание у лифта, который еще не совершал поднятий, должна быть выведена ошибка неправильной
операции. Предусмотреть возможность сравнения какой из лифтов совершил большее количество поднятий.
Также необходимо предусмотреть подсчет общего количества поднятий всех лифтов.
При строчных операциях необходимо вывести детальную информацию по лифту: наименование, количество поднятий и
процент от общего количества поднятий всех лифтов."""


# create class Elevator
class Elevator:
    total_call = 0

    def __init__(self, name):
        self.name = name
        self.call = 0

    def lift(self):
        self.call = self.call + 1
        Elevator.total_call += 1
        return self.call

    def __rsub__(self, value):
        if not self.call and not value:
            raise ValueError('Error: This elevator haven\'t been called')
        return value - self.call

    def __sub__(self, value):
        if not self.call:
            try:
                raise ValueError('Error: This elevator haven\'t been called')
            except ValueError as error:
                print(error)
                return None
        return self.call - value

    def __gt__(self, other):
        return self.call > other

    def __lt__(self, other):
        return self.call < other

    def __repr__(self):
        if Elevator.total_call == 0:
            self.percent = 0
        else:
            self.percent = self.call / Elevator.total_call * 100
        return '\nElevator {} was called {} time(s), it\'s {:.2f} % of the total'.format(self.name, self.call,
                                                                                         self.percent)


# function to input numbers of lifts and check if input is number
def input_num():
    while True:
        input_data = input()
        try:
            inp_num = int(input_data)
            return inp_num
        except ValueError as er:
            print(er, 'INVALID INPUT')
            continue


# create a list of lift's names, we will use to create list instance
def create_names():
    print('Please, enter how many elevators are in your office?')
    quantity_of_elevators = input_num()
    global elevators_names
    elevators_names = []
    elevators_names = [input('Please, enter the name of your elevator: ') for i in range(quantity_of_elevators)]
    return elevators_names


# create list of instance
def create_elevators():
    elevator_list = [Elevator(name) for name in create_names()]
    return elevator_list


# we check if input name is the lift's name and return instance with input name
def check_name_lift(name_lift=None):
    while True:
        if name_lift is None or name_lift not in elevators_names:
            print('\nThere are no such name of the lift')
            name_lift = input('Please enter the name of the elevator you would like to call: ')
        else:
            index = elevators_names.index(name_lift)
            return lifts[index]


# create an empty list
lifts = []
# circle of user's interface to choose what to do with created lifts (call, subtract, compare, etc..)
while True:
    if not lifts:
        lifts = create_elevators()
    what_to_do = input('\nPlease, choose the action you would like to do:\n'
                       '1. call the elevator\n'
                       '2. make subtraction of lifts (only when there are more than one elevator)\n'
                       '3. compare the numbers of call (only when there are more than one elevator)\n'
                       '4. count total calls\n'
                       '5. full information about one elevator\n'
                       '6. quit\n')
    if what_to_do == '1':
        if len(elevators_names) == 1:
            lifts[0].lift()
        else:
            lift = check_name_lift(input('Please enter the name of the elevator you would like to call: '))
            lift.lift()
    elif what_to_do == '2' and len(elevators_names) > 1:  # if we have only one lift this method does'n run
        lift1 = check_name_lift(input('Please enter the name of the elevator #1: '))
        lift2 = check_name_lift(input('Please enter the name of the elevator #2: '))
        print(lift1 - lift2)
    elif what_to_do == '3' and len(elevators_names) > 1:  # if we have only one lift this method does'n run
        lift1 = check_name_lift(input('Please enter the name of the elevator #1: '))
        lift2 = check_name_lift(input('Please enter the name of the elevator #2: '))
        if lift1 > lift2:
            print('\n{} was called {} times more often then {}'.format(lift1.name, lift1 - lift2, lift2.name))
        else:
            print('{} was called {} times more often then {}'.format(lift2.name, lift2 - lift1, lift1.name))
    elif what_to_do == '4':
        print('The total numbers of call is {}'.format(Elevator.total_call))
    elif what_to_do == '5':
        if len(elevators_names) == 1:
            print(lifts[0])
        else:
            print(check_name_lift(input('Please enter the name of the elevator you would like to know')))
    elif what_to_do == '6':
        break
    elif what_to_do[0] not in ['1', '2', '3', '4', '5', '6']:
        print('There are no such action, please choose again: ')
        continue
    else:
        print('\nThere is only one elevator in your office')

# functional test
if __name__ == '__main__':
    Elevator.total_call = 0
    elevators_names = ['lift_1', 'lift_2', 'lift_3', 'lift4']
    lifts = elevators = [Elevator(name) for name in elevators_names]
    print(len(lifts))
    name = elevators_names[0]
    lift1 = check_name_lift(name)
    lift1.lift()
    lift1.lift()
    lift1.lift()
    name = elevators_names[1]
    lift2 = check_name_lift(name)
    lift2.lift()
    lift2.lift()
    name = elevators_names[2]
    lift3 = check_name_lift(name)
    lift3.lift()
    if lift1.call == 3 and lift2.call == 2 and lift3.call == 1:
        print('--- test "Count numbers of call" is OK ---')
    if (lift1 - lift2) == 1 and (lift1 - lift3) == 2:
        print('--- test "Subtraction" is OK ---')
    if (lifts[-1] - lift1) is None:
        print('--- test "Subtraction from non-call lift" is OK ---')
    if lift1 > lift2 and lift3 < lift2:
        print('--- test "Compare" is OK ---')
    if Elevator.total_call == 6:
        print('--- test "Total call" is OK ---')
    print(lift1)

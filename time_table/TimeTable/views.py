from django.shortcuts import render
from .models import Mechanic, Month, TimeTable

# Create your views here.


def mechanic(request):
    mechaninc = Mechanic.objects.all()
    return render(request, 'TimeTable/mechanics.html', context = {'mechanics': mechaninc})


def months(request):
    month = Month.objects.all()
    for item in range(len(month)):
        one_month = month[item]
        one_month = str(one_month)
        days = Month.days_in_month(Month, one_month)
        month[item].number = days
        month[item].save()
        weeks = Month.week_days(Month, days, (item+1))
        print(type(month[item]), 'xxxxxxxxxxxxxxxxxxx')
        month[item].week = weeks
        month[item].save()
    return render(request, 'TimeTable/months.html', context={'month':month, 'days':days})

def timetable(request):
    table = TimeTable.objects.all()
    for item in range(len(table)):
        print(type(table[item]), '111111111111111111111111111')
        ttable = TimeTable.Create_Default_Timetable(TimeTable)
        print(type(table[item]), '222222222222222222222222222')
        table[item].timetable = ttable
        print(type(table[item]), '333333333333333333333333333')
        table[item].save()
    # print(type(table[0]),'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # ttable = TimeTable.Create_Default_Timetable(TimeTable)
    # table.timetable = 2
    # table.timetable.save()
    # print(TimeTable.timetable, '---------------------------------------------------------------')
    return render(request, 'TimeTable/timetable.html', context={'timetable': TimeTable.timetable, 'mech':Mechanic.surname})
from django.db import models
from datetime import datetime, date
import json

# Create your models here.


class Mechanic(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=250)
    timetable_number = models.IntegerField()

    def __str__(self):
        return self.surname


class Month(models.Model):
    month = models.CharField(default='', max_length=20)
    number = models.IntegerField(default=1)
    week = models.CharField(default='', max_length=250)

    def days_in_month(self, month):
        if month == 'April' or month == 'June' or month == 'September' or month == 'November':
            return 30
        elif month == 'February':
            return 28
        else:
            return 31

    def week_days(self, number, month_num):
        week_days = [i+1 for i in range(number)]
        for day in week_days:
            week_day = date(2018, month_num, day).isoweekday()
            week_days[day-1] = week_day
        week_days = json.dumps(week_days)
        return week_days

    def __str__(self):
        return self.month


class TimeTable(models.Model):
    mechanic_id = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    month_id = models.ForeignKey(Month, on_delete=models.CASCADE)
    timetable = models.CharField(default='', max_length=250)

    def Create_Default_Timetable(self):
        name = Mechanic.surname
        dict = [1 for i in range(30)]
        for key in dict:
            if dict[key] == 1 and key < 4:
                # first_num = input('Введите первую смену:')
                # first_num = int(first_num)
                dict[key] = 1#first_num
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 21 and dict[key - 1] == 7:
                dict[key] = 0
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 14 and dict[key - 1] == 0:
                dict[key] = 0
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 7 and dict[key - 1] == 0:
                dict[key] = 23
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 23 and dict[key - 1] == 23:
                dict[key] = 23
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 46 and dict[key - 1] == 23:
                dict[key] = 23
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 69 and dict[key - 1] == 23:
                dict[key] = 0
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 46 and dict[key - 1] == 0:
                dict[key] = 0
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 23 and dict[key - 1] == 0:
                dict[key] = 15
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 15 and dict[key - 1] == 15:
                dict[key] = 15
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 30 and dict[key - 1] == 15:
                dict[key] = 15
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 45 and dict[key - 1] == 15:
                dict[key] = 0
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 30 and dict[key - 1] == 0:
                dict[key] = 0
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 15 and dict[key - 1] == 0:
                dict[key] = 7
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 7 and dict[key - 1] == 7:
                dict[key] = 7
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 14 and dict[key - 1] == 7:
                dict[key] = 7
            elif (dict[key - 3] + dict[key - 2] + dict[key - 1]) == 21 and dict[key - 1] == 7:
                dict[key] = 0
        #time_table = {name:dict}
        time_table = json.dumps(dict)
        return time_table
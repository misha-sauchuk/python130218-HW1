from django.forms import ModelForm, modelformset_factory
from django import forms
from .models import Mechanic, Month, Timetable
from datetime import datetime, date
import calendar
import json
from random import shuffle


class AddMechanic(ModelForm):
    class Meta:
        model = Mechanic
        fields = ['name', 'surname', 'phone', 'address', 'timetable_number']


class ModifyMechanic(ModelForm):
    class Meta:
        model = Mechanic
        fields = ['phone', 'address']


class ChooseMonth(ModelForm):

    class Meta:
        model = Month
        fields = ['month', 'name', 'days_in_month', 'week_days', 'public_holidays', 'free_days', 'working_days']
        widgets = {
            'name': forms.HiddenInput,
            'days_in_month': forms.HiddenInput,
            'week_days': forms.HiddenInput,
            'working_days': forms.HiddenInput
        }

    def clean(self):
        cleaned_data = super().clean()

        # check if this moth haven't been created yet
        month_created = Month.objects.all()
        for month in month_created:
            if cleaned_data['month'] == month.month:
                raise forms.ValidationError('The {} is already created'.format(month.name))

        # found the amount of days in the current month
        month = int(cleaned_data['month'])
        cleaned_data['name'] = calendar.month_name[month]

        month_info = calendar.monthrange(2018, month)
        cleaned_data['days_in_month'] = month_info[1]

        # check if the order of month is correct
        if month > 1:
            try:
                Month.objects.get(month=(month-1))
            except:
                raise forms.ValidationError ('You try to create month in incorrect order')

        # create list of week days where 1 is Monday, 2 is Tuesday and etc.
        week_days = [(date(2018, month, day).isoweekday()) for day in range(1, month_info[1] + 1)]
        cleaned_data['week_days'] = json.dumps(week_days)

        # calculating the amount of working days in the current month
        working_days = len(list(filter((lambda x: x < 6), week_days)))

        # check if there are public_holidays in weekdays (Monday - Friday)
        if cleaned_data['public_holidays'] is not None:
            public_holidays = cleaned_data['public_holidays'].split(',')
            for item in public_holidays:
                if week_days[int(item) - 1] < 6:
                    working_days -= 1
            cleaned_data['working_days'] = working_days
        else:
            cleaned_data['working_days'] = working_days
        return cleaned_data


class CreateTimetable(ModelForm):
    class Meta:
        model = Timetable
        fields = ['mechanic_id', 'month_id', 'start_with', 'timetable']
        widgets = {
            'timetable': forms.HiddenInput
        }

    def clean(self):
        cleaned_data = super().clean()

        # check if there are only one timetable for this mechanic at this month
        timetable = Timetable.objects.all()
        for item in timetable:
            if cleaned_data['mechanic_id'] == item.mechanic_id and cleaned_data['month_id'] == item.month_id:
                raise forms.ValidationError('The timetable for {} is created'.format(cleaned_data['mechanic_id']))

        month_id = cleaned_data['month_id']
        month = int(month_id.month)  # find number of months in Month objects
        if month > 1:
            try:
                timetable_pre = Timetable.objects.get(month_id__month=(month - 1),
                                                      mechanic_id=cleaned_data['mechanic_id'])
            except:
                raise forms.ValidationError('You try to create timetable in incorrect order')

        try:
            # try to create temporary timetable to find first three shifts
            end_with = json.loads(timetable_pre.timetable)[-3:]
            list_shift_start = create_base_shift(6, end_with)
            start_with = list_shift_start[-3:]
        except:
            start_with = cleaned_data['start_with'].split(',')
            start_with = [int(x) for x in start_with]

        list_shift = create_base_shift(month_id.days_in_month, start_with)  # create basic timetable

        # create list with index of all Mondays (the first day in week) in month
        week_days = json.loads(month_id.week_days)
        day_list = create_day_index(1, week_days)

        # add to our timetable shift on Monday
        list_shift = add_shift_on_monday(day_list,list_shift)

        # find the amount working days in timetable
        sum = 0
        for item in list_shift:
            if item > 0:
                sum += 1

        # shuffle_days = [i + 1 for i in range(len(list_shift))]
        # shuffle(shuffle_days)
        # for day in shuffle_days:

        # add shifts to timetable to finish the timetable
        list_shift = get_full_timetable(list_shift, sum, month_id.working_days, week_days)

        cleaned_data['timetable'] = json.dumps(list_shift)
        return cleaned_data


class ModTimetable(ModelForm):
    SHIFT = ((0,'free day'), (7,'first shift'), (15,'second shift'), (23,'third shift'))
    free_day = forms.IntegerField(required=False)
    day = forms.IntegerField()
    shift = forms.ChoiceField(choices=SHIFT)

    class Meta:
        model = Timetable
        fields = ['timetable','day', 'shift', 'free_day']
        widgets = {
            'timetable': forms.HiddenInput
        }

    def clean(self):
        cleaned_data = super().clean()
        day = cleaned_data['day']
        free_day = cleaned_data['free_day']
        timetable = json.loads(cleaned_data['timetable'])
        working_days = len(list(filter((lambda x: x > 0), timetable)))
        shift = int(cleaned_data['shift'])
        timetable[day-1] = shift
        if free_day:
            timetable[free_day-1] = 0
        working_days_mod = len(list(filter((lambda x: x > 0), timetable)))
        if working_days != working_days_mod:
            raise forms.ValidationError('You should add a free day')
        cleaned_data['timetable'] = json.dumps(timetable)
        return cleaned_data


def create_base_shift(amount_of_days, start_list):
    dict = {x: 1 for x in range(amount_of_days)}
    for key in dict:
        if dict[key] == 1 and key < 3:
            dict[key] = start_list[key]
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
    list_shift = []
    for key in dict:
        list_shift.append(dict[key])
    return list_shift


def create_day_index(number_of_day, week_days):
    d = 0
    day_list = []
    for day in week_days:
        if day == number_of_day:
            day_list.append(d)
        d += 1
    return day_list


def add_shift_on_monday(day_list,list_shift):
    for id in day_list:
        if id < (len(list_shift) - 1) and ((list_shift[id] == 0 and list_shift[id + 1] == 15) or (
                list_shift[id] == 0 and list_shift[id - 1] == 15)) or (
                id > 0 and list_shift[id] == 0 and list_shift[id - 1] == 0 and list_shift[id - 2] == 23):
            list_shift[id] = 15
    return list_shift


def get_full_timetable(list_shift, not_all_working_days, working_days, week_days):
    for_list = [i for i in range(len(list_shift))]
    shuffle(for_list)
    print(for_list)
    for day in for_list:
        if not_all_working_days < working_days:
            if (list_shift[day] == 0 and week_days[day] < 6 and list_shift[day + 1] == 7 and list_shift[
                day - 1] == 0) or (
                    day > 0 and list_shift[day] == 0 and week_days[day] < 6 and list_shift[day - 1] == 7 and
                    list_shift[day + 1] == 0):
                list_shift[day] = 7
                not_all_working_days += 1
            elif (list_shift[day] == 0 and week_days[day] < 6 and list_shift[day + 1] == 15 and list_shift[
                day - 1] == 0) or (
                    day > 0 and list_shift[day] == 0 and week_days[day] < 6 and list_shift[day - 1] == 15 and
                    list_shift[day + 1] == 0):
                list_shift[day] = 15
                not_all_working_days += 1
            elif (list_shift[day] == 0 and week_days[day] < 6 and list_shift[day + 1] == 23 and list_shift[
                day - 1] == 0) or (
                    day > 0 and list_shift[day] == 0 and week_days[day] < 6 and list_shift[day - 1] == 23 and
                    list_shift[day + 1] == 0):
                list_shift[day] = 23
                not_all_working_days += 1
    return list_shift
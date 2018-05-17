from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Mechanic, Month, Timetable
from .forms import AddMechanic, ChooseMonth, CreateTimetable, ModifyMechanic, ModTimetable
import datetime
import calendar
from django.contrib.auth.decorators import login_required, permission_required
import json

# Create your views here.


def home_page(request):
    current_month = datetime.datetime.today().month
    current_year = datetime.datetime.today().year
    month_name = calendar.month_name[current_month]
    days = calendar.monthrange(current_year, current_month)
    current_month = str(current_month)
    days_list=[i+1 for i in range(days[1])]
    timetable = Timetable.objects.filter(month_id__month = current_month)
    table_list = []
    for t in timetable:
        name = '{} {}'.format(t.mechanic_id.name, t.mechanic_id.surname)
        mech_id = t.mechanic_id.id
        t_table = json.loads(t.timetable)
        timetable_id = t.id
        table_tuple = (name, t_table, timetable_id, mech_id)
        table_list.append(table_tuple)
    return render(request, 'home.html', context={'month_name': month_name,
                                                 'table_list': table_list,
                                                 'days': days_list})


@login_required()
def mechanic(request):
    mechanincs = Mechanic.objects.all()
    return render(request, 'mechanics.html', context={'mechanics': mechanincs})


@login_required()
def mechanic_info(request, mechanic_id, mechanic_name):
    mechanic = Mechanic.objects.get(id=mechanic_id)
    table = mechanic.table.all()
    mech_list = []
    for item in table:
        timetable = json.loads(item.timetable)
        month = item.month_id
        month_id = item.month_id.id
        days = item.month_id.days_in_month
        days_l = [i+1 for i in range(days)]
        mech_tuple = (month,timetable, days_l, month_id)
        mech_list.append(mech_tuple)
    return render(request, 'mechanic_info.html', context={'mechanic': mechanic, 'mech_list':mech_list})


@permission_required('TimeTable.can_add_mechanic')
@login_required()
def add_mechanic(request):
    form = AddMechanic()
    if request.method == 'POST':
        form = AddMechanic(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mechanics')
    return render(request, 'add_mechanic.html', context={'add_mechanic': form})


@permission_required('TimeTable.can_add_mechanic')
@login_required()
def modify_mechanic(request, mechanic_id):
    mechanic = Mechanic.objects.get(id=mechanic_id)

    if request.method == 'POST':
        form = ModifyMechanic(request.POST, instance=mechanic)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mechanics/{}'.format(mechanic_id))
    form = ModifyMechanic(instance=mechanic)
    return render(request, 'mod_mechanic.html', context={'mod_mechanic': form, 'mechanic': mechanic})


@login_required()
def months(request):
    months = Month.objects.all()
    return render(request, 'months.html', context={'month': months})


@login_required()
def month_info(request, month_id, month_name):
    month = Month.objects.get(id=month_id)
    days = month.days_in_month
    days_list = [i+1 for i in range(days)]
    table = month.month_name.all()
    month_list = []
    for item in table:
        mechanic = item.mechanic_id
        mech_id = item.mechanic_id.id
        timetable = json.loads(item.timetable)
        month_tuple = (mechanic,timetable,mech_id)
        month_list.append(month_tuple)
    return render(request, 'month_info.html', context={'month': month, 'month_list':month_list, 'days':days_list})


@permission_required('TimeTable.can_add_month')
@login_required()
def choose_month(request):
    form = ChooseMonth()
    if request.method == 'POST':
        form = ChooseMonth(request.POST)
        if form.is_valid():
            #print('before save')
            form.save()
            #print('after save')
            return HttpResponseRedirect('/months')
    return render(request, 'choose_month.html', context={'choose_month': form})


@login_required()
def timetable(request):
    timetable = Timetable.objects.all()
    months = Month.objects.all()
    month_list_all = []
    for month in months:
        days = month.days_in_month
        days_list = [i + 1 for i in range(days)]
        table = month.month_name.all()
        month_list = []
        for item in table:
            mechanic = item.mechanic_id
            mech_id = item.mechanic_id.id
            timetable = json.loads(item.timetable)
            month_tuple = (mechanic, timetable, mech_id)
            month_list.append(month_tuple)
        month_tuple_all = (month.name, days_list,month_list, month.id)
        month_list_all.append(month_tuple_all)
    return render(request, 'timetable.html', context={'timetable': timetable,
                                                      'month':months,
                                                      'table_list':month_list_all})


@permission_required('TimeTable.can_add_mod_timetable')
@login_required()
def create_timetable(request):
    form = CreateTimetable()
    if request.method == 'POST':
        form = CreateTimetable(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/timetable')
    return render(request, 'create_timetable.html', context={'create_timetable': form})


@permission_required('TimeTable.can_add_mod_timetable')
@login_required()
def modify_timetable(request, timetable_id):
    timetable = Timetable.objects.get(id=timetable_id)
    table = json.loads(timetable.timetable)
    mech_name = timetable.mechanic_id
    days = timetable.month_id.days_in_month
    days_list = [i+1 for i in range(days)]
    table_tuple = [mech_name,table,days_list]

    if request.method == 'POST':
        form = ModTimetable(request.POST, instance=timetable)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = ModTimetable(instance=timetable)
    return render(request, 'mod_timetable.html', context={'mod_timetable': form,
                                                          'timetable': timetable,
                                                          'table_tuple': table_tuple})


@login_required()
def search(request):
    q = request.GET.get('q')
    weekday_list = list(calendar.day_name)
    if q:
        date = q.split('-')
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        current_month = datetime.datetime.today().month
        weekday = weekday_list[calendar.weekday(year,month,day)]
        timetable = Timetable.objects.filter(month_id__month = month)
        result_search = []
        for t in timetable:
            name = '{} {}'.format(t.mechanic_id.name, t.mechanic_id.surname)
            mech_id = t.mechanic_id.id
            t_table = json.loads(t.timetable)[day-1]
            timetable_id = t.id
            table_tuple = (name, t_table, timetable_id, mech_id)
            result_search.append(table_tuple)
        return render(request, 'search.html', context={'result_search': result_search,
                                                       'q': q,
                                                       'weekday': weekday,
                                                       'current_month': current_month,
                                                       'month': month})
    return render(request, 'search.html')



# d2 = {'free_days': None, 'public_holidays': None, 'week_days': '[6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1]', 'month': '12', 'working_days': 21, 'days_in_month': 31, 'name': 'December'}
#
# d1 = {'month': '12', 'name': 'December', 'free_days': None, 'week_days': '[6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1]', 'working_days': 21, 'days_in_month': 31, 'public_holidays': None}
#
# if d1 == d2:
#     print('ok')
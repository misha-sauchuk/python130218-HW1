from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Mechanic, Month, Timetable
from .forms import AddMechanic, ChooseMonth, CreateTimetable, ModifyMechanic, ModTimetable
import datetime
import calendar
# Create your views here.


def home_page(request):
    timetable = Timetable.objects.all()
    current_month = datetime.datetime.today().month
    month_name = calendar.month_name[current_month]
    current_month = str(current_month)
    return render(request, 'home.html', context={'timetable': timetable, 'month': current_month, 'month_name': month_name})


def mechanic(request):
    mechanincs = Mechanic.objects.all()
    return render(request, 'mechanics.html', context={'mechanics': mechanincs})


def mechanic_info(request, mechanic_id):
    mechanic = Mechanic.objects.get(id=mechanic_id)
    return render(request, 'mechanic_info.html', context={'mechanic': mechanic})


def add_mechanic(request):
    form = AddMechanic()
    if request.method == 'POST':
        form = AddMechanic(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/table/mechanics')
    return render(request, 'add_mechanic.html', context={'add_mechanic': form})


def modify_mechanic(request, mechanic_id):
    mechanic = Mechanic.objects.get(id=mechanic_id)

    if request.method == 'POST':
        form = ModifyMechanic(request.POST, instance=mechanic)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/table/mechanics/{}'.format(mechanic_id))
    form = ModifyMechanic(instance=mechanic)
    return render(request, 'mod_mechanic.html', context={'mod_mechanic': form, 'mechanic': mechanic})


def months(request):
    months = Month.objects.all()
    return render(request, 'months.html', context={'month':months})


def month_info(request, month_id):
    month = Month.objects.get(id=month_id)
    return render(request, 'month_info.html', context={'month':month})


def choose_month(request):
    form = ChooseMonth()
    if request.method == 'POST':
        form = ChooseMonth(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/table/months')
    return render(request, 'choose_month.html', context={'choose_month': form})


def timetable(request):
    timetable = Timetable.objects.all()#get(month = month)
    return render(request, 'timetable.html', context={'timetable': timetable})


def create_timetable(request):
    form = CreateTimetable()
    if request.method == 'POST':
        form = CreateTimetable(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/table/timetable')
    return render(request, 'create_timetable.html', context={'create_timetable': form})


def modify_timetable(request, timetable_id):
    timetable = Timetable.objects.get(id=timetable_id)

    if request.method == 'POST':
        form = ModTimetable(request.POST, instance=timetable)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/table/home')
    form = ModTimetable(instance=timetable)
    return render(request, 'mod_timetable.html', context={'mod_timetable': form, 'timetable':timetable})






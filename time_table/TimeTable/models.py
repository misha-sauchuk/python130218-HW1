from django.db import models
from django.contrib.auth.models import User
#from django_mysql.models import JSONField, Model

# Create your models here.


class Mechanic(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=250)
    timetable_number = models.IntegerField(unique=True)
    # image = models.ImageField(default='', upload_to='media/images', blank=True)

    class Meta:
        permissions = (('can_add_mod_mechanic', 'Create and modify mechanic'),)

    def __str__(self):
        if self.name is None or self.surname is None:
            return "ERROR NAME OR SURNAME IS NULL"
        return '{} {}'.format(self.name, self.surname)


class Month(models.Model):
    MONTHS = (
    ('1', 'January'), ('2', 'February'), ('3', 'March',), ('4', 'April'), ('5', 'May',), ('6', 'June'), ('7', 'Jule'),
    ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December'))
    month = models.CharField(default='', max_length=200, choices=MONTHS)
    name = models.CharField(default='', max_length=50, null=True, blank=True)
    days_in_month = models.IntegerField(default='', null=True, blank=True)
    week_days = models.CharField(default='', max_length=250, null=True, blank=True)

    public_holidays = models.CharField(default='', max_length=20, null=True, blank=True, help_text='Enter the the days '
                                                                                                   'of public holidays '
                                                                                                   'in this month. If '
                                                                                                   'there are several '
                                                                                                   'holidays, please '
                                                                                                   'enter in one line '
                                                                                                   'with comma-'
                                                                                                   'separate')
    free_days = models.CharField(default='', max_length=20, null=True, blank=True, help_text='Enter the day that '
                                                                                             'is free of work. If '
                                                                                             'there are several '
                                                                                             'days, please '
                                                                                             'enter in one line '
                                                                                             'with comma-separate')
    working_days = models.IntegerField(default=None, null=True, blank=True)

    class Meta:
        permissions = (('can_add_month', 'Create a month'),)

    def __str__(self):
        if self.name is None:
            return "ERROR NAME IS NULL"
        return self.name


class Timetable(models.Model):
    mechanic_id = models.ForeignKey(Mechanic, on_delete=models.CASCADE, related_name='table')
    month_id = models.ForeignKey(Month, on_delete=models.CASCADE, related_name='month_name')
    start_with = models.CharField(default='', max_length=20, null=True, blank=True, help_text='Enter 3 first days in '
                                                                                              'the timetable.'
                                                                                              ' The correct format is: '
                                                                                              ' \'d,d,d\','
                                                                                              ' 0 - is free day; '
                                                                                              '23 - is first shift; '
                                                                                              '7 - is second shift; '
                                                                                              '15 - is third shift ')
    timetable = models.CharField(default='', max_length=250, null=True, blank=True)

    class Meta:
        permissions = (('can_add_mod_timetable', 'Create and modify timetable'),)
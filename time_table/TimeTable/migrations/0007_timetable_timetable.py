# Generated by Django 2.0.4 on 2018-04-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0006_month_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='timetable',
            field=models.CharField(default='', max_length=250),
        ),
    ]

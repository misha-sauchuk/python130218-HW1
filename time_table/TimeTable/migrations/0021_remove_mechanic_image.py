# Generated by Django 2.0.4 on 2018-05-16 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0020_auto_20180517_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mechanic',
            name='image',
        ),
    ]

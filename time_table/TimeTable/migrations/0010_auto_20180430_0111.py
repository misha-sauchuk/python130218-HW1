# Generated by Django 2.0.4 on 2018-04-29 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0009_auto_20180430_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='month',
            field=models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'Jule'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default='', max_length=200),
        ),
    ]

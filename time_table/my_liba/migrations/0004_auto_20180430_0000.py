# Generated by Django 2.0.4 on 2018-04-29 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_liba', '0003_auto_20180426_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='years',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-23 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210323_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='bdate',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='bpeople',
            new_name='people',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='bphone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='bsgm',
            new_name='sgm',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='btime',
            new_name='time',
        ),
    ]

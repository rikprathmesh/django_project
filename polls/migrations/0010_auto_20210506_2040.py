# Generated by Django 3.1.7 on 2021-05-06 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_menu_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='bname',
            new_name='bnme',
        ),
    ]

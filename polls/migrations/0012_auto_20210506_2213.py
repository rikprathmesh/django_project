# Generated by Django 3.1.7 on 2021-05-06 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20210506_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='sgm',
            new_name='msg',
        ),
    ]
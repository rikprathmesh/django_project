# Generated by Django 3.1.7 on 2021-03-23 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210324_0131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='sgm',
            new_name='msg',
        ),
    ]

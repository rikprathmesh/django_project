# Generated by Django 3.1.7 on 2021-03-23 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=200)),
                ('bemail', models.EmailField(max_length=100)),
                ('bphone', models.CharField(max_length=20)),
                ('bdate', models.DateField()),
                ('btime', models.TimeField()),
                ('bpeople', models.CharField(max_length=100)),
                ('bsgm', models.TextField(max_length=500)),
            ],
        ),
    ]
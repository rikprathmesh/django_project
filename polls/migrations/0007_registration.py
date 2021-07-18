# Generated by Django 3.1.7 on 2021-04-04 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20210324_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reg_name', models.CharField(max_length=50)),
                ('Reg_lname', models.CharField(max_length=50)),
                ('Reg_email', models.EmailField(max_length=50)),
                ('Reg_contact', models.CharField(max_length=20)),
                ('Reg_password1', models.CharField(max_length=20)),
                ('Reg_password2', models.CharField(max_length=20)),
            ],
        ),
    ]

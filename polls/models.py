from django.db import models

# Create your models here.


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    feedback = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class booking(models.Model):
    bname = models.CharField(max_length=200)
    bemail = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.CharField(max_length=100)
    msg = models.TextField(max_length=500)


class registration(models.Model):
    Reg_name = models.CharField(max_length=50)
    Reg_lname = models.CharField(max_length=50)
    Reg_email = models.EmailField(max_length=50)
    Reg_contact = models.CharField(max_length=20)
    Reg_password1 = models.CharField(max_length=20)
    Reg_password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.Reg_name


class menu(models.Model):
    menu_name = models.CharField(max_length=50)
    menu_desc = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="media/recepies", default="NA")
    menu_price = models.CharField(max_length=50)

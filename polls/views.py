from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import contact, booking, registration, menu
from datetime import datetime
from django.contrib import messages
from django.urls import reverse
import razorpay
# Create your views here.


def index(request):
    if request.method == 'POST':
        if userlog is not None:
            name = request.POST['name']
            email = request.POST['email']
            feedback = request.POST['feedback']
            Contact = contact(name=name, email=email, feedback=feedback)
            Contact.save()
            return render(request, 'index.html', {'userlog': userlog})
    return render(request, 'index.html')


def booking1(request):
    if request.method == "POST":

        bname = request.POST['bname']
        bemail = request.POST['bemail']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        msg = request.POST['msg']

        Booking = booking(bname=bname, bemail=bemail, phone=phone,
                          date=date, time=time, people=people, msg=msg)
        Booking.save()
        return render(request, 'index.html')


def registration1(request):
    if request.method == "POST":

        Reg_name = request.POST['reg_name']
        Reg_lname = request.POST['reg_lname']
        Reg_email = request.POST['reg_email']
        Reg_contact = request.POST['reg_contact']
        Reg_password1 = request.POST['reg_password1']
        Reg_password2 = request.POST['reg_password2']

        Registration = registration(Reg_name=Reg_name, Reg_lname=Reg_lname, Reg_email=Reg_email, Reg_contact=Reg_contact,
                                    Reg_password1=Reg_password1, Reg_password2=Reg_password2)
        Registration.save()
        return redirect('login')
        # Registration.Reg_name = Reg_name
        # Registration.Reg_lname = Reg_lname
        # Registartion.Reg_email = Reg_email
        # Registartion.Reg_contact = Reg_contact
        # Registartion.Reg_password1 = Reg_password1
        # Registartion.Reg_password2 = Reg_password2

        # Registartion.save()
    return render(request, 'registration.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

# def contact(request):
#    return render(request,"<script>alert('Form Submitted Successfully')</script>")


def login(request):
    if request.method == 'POST':
        useremail = request.POST['lemail']
        userpass = request.POST['lpassword']
        global userlog
        userlog = get_object_or_404(
            registration, Reg_email=useremail, Reg_password1=userpass)

        if userlog != None:
            return render(request, 'index.html', {'userlog': userlog})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

    return render(request, 'login.html')


def menu1(request):
    Menu = menu.objects.all()
    if request.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(
            auth=('rzp_test_j7UraQ9urJjUdq', 'S6Ys0OL45ol1s6bTntNx9mDD'))
        payment = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        messages.success(request, 'Thank You for Ordering')
        return redirect('menu')

    data = {
        'menus': Menu
    }
    return render(request, 'menu.html', data)

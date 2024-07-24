from django.shortcuts import render,redirect
from Hospitalapp.models import appointment


# Create your views here.
def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'doctors.html')


def Appointment(request):
   if request.method == 'POST':
       appointments = appointment(
           name = request.POST['name'],
           email = request.POST['email'],
           phone = request.POST['phone'],
           date = request.POST['date'],
           doctor = request.POST['doctor'],
           department = request.POST['department'],
           message = request.POST['message']
            )

       appointments.save()
       return redirect("/appointment")
   else:
       return render(request,'appointment.html')
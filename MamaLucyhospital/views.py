from django.shortcuts import render,redirect
from Hospitalapp.models import appointment, patient


# Create your views here.
def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'doctors.html')
def show(request):
   myappointments = appointment.objects.all()
   return render(request, 'show.html',{'appointments':myappointments})

# create a function for delete
def delete(request,id):
    Appointment = appointment.objects.get(id=id)
    Appointment.delete()
    return redirect("/show")

def clients(request):
   myclients = patient.objects.all()
   return render(request,'clients.html',{'patients':myclients})
def Delete(request,id):
    Patient= patient.objects.get(id=id)
    Patient.delete()
    return redirect("/clients")
def edit(request):
    return render(request,'edit.html')



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
       return redirect("/show")
   else:
       return render(request,'appointment.html')
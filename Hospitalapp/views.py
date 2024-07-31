import json

import requests
from django.http import HttpResponse
from django.shortcuts import render,redirect
from requests.auth import HTTPBasicAuth

from Hospitalapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from Hospitalapp.models import appointment, patient
from Hospitalapp.forms import appointmentForm


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
def edit(request,id):
    editappointment = appointment.objects.get(id=id)
    return render(request,'edit.html',{'appointment':editappointment})
def update(request,id):
    updateinfo= appointment.objects.get(id=id)
    form = appointmentForm(request.POST,instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html')

# for appointment page

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


# a page for pay.html

def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": " sheila Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("payment made successfully")
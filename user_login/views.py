from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import Psychologist, Appointment
from django.urls import reverse
from django.contrib import messages


def user_login(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you logged on')            
            return redirect('home')
        else:            
            return render(request, 'user_login.html')
    else:
        return render(request, 'user_login.html')
    

def home(request):
    if request.user.is_authenticated:
        psy = Psychologist.objects.all()
        context = {'psy':psy}
        return render(request, 'home.html', context)
    else:
        return redirect(reverse(user_login))
    
def user_logout(request):
    logout(request)
    return redirect('user_login')

def add_psy(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['fname'] !=" " and request.POST['lname'] !=" " and request.POST['category'] !=" " and request.POST['experience'] !=" " and request.POST['hour_price'] !=" ": 
                psy = Psychologist()
                psy.fname = request.POST['fname']
                psy.lname = request.POST['lname']
                psy.category = request.POST['category']
                psy.experience = request.POST['experience']
                psy.hour_price = request.POST['hour_price']
                psy.save()
                return redirect('home')
            else:
                return render(request, 'add_psy.html')
        else:            
            return render(request, 'add_psy.html')
    else:
        return redirect(reverse(user_login))

@login_required
def update_psy(request, id):
    update_info = Psychologist.objects.get(id=id)
    context = {'update_info':update_info}
    if request.method == 'POST':
        update_info.fname = request.POST['fname']
        update_info.lname = request.POST['lname']
        update_info.category = request.POST['category']
        update_info.experience = request.POST['experience']
        update_info.hour_price = request.POST['hour_price']
        update_info.save()
        return redirect('home')
    else:
        return render(request, 'update_psy.html', context)

@login_required
def delete_psy(request,id):
    psy = Psychologist.objects.get(id=id)
    if request.method == 'POST':
        psy.delete()
        return redirect('home')
    else:
        context = {'psy':psy}
        return render(request, 'delete_psy.html', context)
    
@login_required
def records(request, id):
    all_records = Appointment.objects.filter(psychologist_id = id).order_by('date', 'time')
    psy = Psychologist.objects.get(id=id)
    context = {'all_records':all_records, 'psy':psy}
    return render(request, 'records.html', context)
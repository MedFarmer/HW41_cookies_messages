from django.shortcuts import render, redirect
from .models import Psychologist, Appointment

def index(request):
    return render(request, 'index.html')

def psychologist(request):
    psy = Psychologist.objects.all()
    context = {'psy':psy}
    return render(request, 'psychologist.html', context)

def contact_us(request):
    return render(request, 'contact_us.html')

def appointment(request, id):
    psy = Psychologist.objects.get(id=id)
    context = {'psy':psy}  
    is_busy = 'yes'
    if request.method == 'POST':
        record = request.POST     
        if record['client_fname'] !='' and record['client_lname'] != '' and record['date'] != "" and record['time'] != '': 
            appointing = Appointment()
            appointing.client_fname = record['client_fname']
            appointing.client_lname = record['client_lname']
            appointing.date = record['date']
            appointing.time = record['time']
            appointing.psychologist_id = id
            if_busy = Appointment.objects.filter(psychologist_id = id, date = appointing.date, time = appointing.time)
            if if_busy:
                context = {'psy':psy,'is_busy':'yes'}
                return render(request, 'appointment.html', context)
            else:             
                appointing.clean_fields()
                appointing.save()
                context = {'psy':psy, 'appointing':appointing}            
                return render(request, 'record_message.html', context)               
        else:
            return render(request, 'appointment.html', context)
    else:
        return render(request, 'appointment.html', context)
    
def record_message(request):
    return render(request, 'record_message.html')

def update_appointment(request):   
    if request.method == 'POST':
        record = request.POST
        client_fname = record['client_fname']
        client_lname = record['client_lname']
        get_info = Appointment.objects.filter(client_fname = client_fname, client_lname = client_lname)
        
        time = None
        date = None
        id = None
        
        for each in get_info:
            client_id = each.id
            time = each.time
            date = each.date
            id = each.psychologist_id
        if id is not None:
            psy = Psychologist.objects.get(id=id)
            psy_fname = psy.fname
            psy_lname = psy.lname
            context = {'psy_fname':psy_fname, 'psy_lname':psy_lname, 'time':time, 'date':date, 'client_id':client_id}            
        else:
            context = {'error_message': 'По вашему имени нет записи!'}
    else:
        context = {}
    return render(request, 'update_appointment.html', context)

def update_appointment1(request, id):    
    update_info = Appointment.objects.get(id=id)
    context = {'appointing':update_info}
    if request.method == 'POST':
        update_info.client_fname = request.POST['client_fname']
        update_info.client_lname = request.POST['client_lname']
        update_info.date = request.POST['date']
        update_info.time = request.POST['time']
        psy = Psychologist.objects.get(id=update_info.psychologist.id)
        if_busy = Appointment.objects.filter(psychologist_id = update_info.psychologist.id, date = update_info.date, time = update_info.time)
        if if_busy:
            context = {'psy':psy,'is_busy':'yes'}
            return render(request, 'update_appointment1.html', context)
        else:
            update_info.save()            
            context = {'psy':psy, 'appointing':update_info}
            return render(request, 'record_message.html', context)
    else:
        return render(request, 'update_appointment1.html', context)
    
def delete_appointment(request):
    if request.method == 'POST':
        record = request.POST
        client_fname = record['client_fname']
        client_lname = record['client_lname']
        if client_fname != '' and client_lname != '':
            get_info = Appointment.objects.filter(client_fname = client_fname, client_lname = client_lname)
            if get_info:
                get_info.delete()
                context = {'is_deleted':'yes'}
                return render(request, 'delete_appointment.html', context)
            else:
                return render(request, 'delete_appointment.html')
        else:
            return render(request, 'delete_appointment.html')
    else:
        return render(request, 'delete_appointment.html')
    


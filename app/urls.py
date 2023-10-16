from django.contrib import admin
from django.urls import path, include
from .views import index, psychologist, contact_us, appointment, update_appointment, update_appointment1, record_message, delete_appointment

urlpatterns = [   
    path('', index, name='index'),
    path('psychologist/', psychologist, name='psychologist'),
    path('contact_us/', contact_us, name='contact_us'),
    path('appointment/<int:id>', appointment, name='appointment'),
    path('appointment/message/', record_message, name='record_message'),
    path('update_appointment/', update_appointment, name='update_appointment'),    
    path('update_appointment/<int:id>', update_appointment1, name='update_appointment1'),
    path('delete_appointment/', delete_appointment, name='delete_appointment'),
    
]

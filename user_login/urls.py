from django.contrib import admin
from django.urls import path
from .views import user_login, home, user_logout, add_psy, update_psy, delete_psy, records

urlpatterns = [   
    path('', user_login, name='user_login'),
    path('home/', home, name='home'),  
    path('logout/', user_logout, name='user_logout'),
    path('add_psy/', add_psy, name='add_psy'),
    path('update_psy/<int:id>', update_psy, name='update_psy'),
    path('delete_psy/<int:id>', delete_psy, name='delete_psy'),
    path('records/<int:id>', records, name='records'),
]
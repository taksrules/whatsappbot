from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='home'),
               path('c80821c-2d9c-46c5-9049-b4c56b1b469e', views.whatsAppWebhook, name='whatsapp-web'),               
               ]

#https://taskrules.pythonanywhere.com/c80821c-2d9c-46c5-9049-b4c56b1b469e
#070ac4a2-76fe-4014-b31b-998e393f0264
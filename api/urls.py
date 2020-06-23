from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('send_aritime', views.send_aritime, name='send_aritime'),
   path('display_result', views.display_result, name='display_result')
]


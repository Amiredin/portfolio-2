from django.urls import path 
from .import views


urlpatterns=[
     path('', views.home, name='portfolio-home'),
     path('about/', views.about, name='portfolio-about'),
     path('work/', views.work, name='portfolio-work'),

]
# from django.urls import url
from django.urls import path
import views

urlpatterns = [
    path('home/',views.home_page,name='home'),
]
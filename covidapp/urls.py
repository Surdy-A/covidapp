
from django.contrib import admin
from django.urls import path
from .views import covid_data_view

urlpatterns = [
    path('', covid_data_view),
]

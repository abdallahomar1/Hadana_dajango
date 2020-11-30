from django.urls import path
from . import views
app_name = 'daragat'
urlpatterns = [
    path('', views.all_darajat),
]
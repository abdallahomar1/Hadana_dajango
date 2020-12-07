from django.urls import path
from . import views
app_name = 'daragat'
urlpatterns = [
    path('<int:id>', views.my, name= 'my_view'),
    path('', views.all_darajat),
    path('all', views.all_shah),
]
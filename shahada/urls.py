from django.urls import path
from . import views
app_name = 'student'
urlpatterns = [
    path('<int:id>', views.my, name='student_datail'),
]
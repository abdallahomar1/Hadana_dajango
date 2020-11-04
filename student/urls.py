from django.urls import path
#from student.views import all_student, student_one
from . import views
app_name = 'student'
urlpatterns = [
    path('', views.all_student),
    path('<int:id>', views.student_one, name='student_datail')
]
from django.urls import path
from . import views
app_name = 'student'
urlpatterns = [
    path('', views.all_student),
    path('<int:id>', views.student_one, name='student_datail'),
    path('rebh', views.rebh),
    path('employees', views.employees),
    path('sadr/<int:id>', views.employees_one, name='employees'),
    path('keyab', views.alkeyab),
    path('keyabs', views.myfun),
    path('myshahda/<int:id>', views.my, name='my'),
    path('talemat', views.talemat),
]
from django.urls import path,include
from .views import student_add_update, student_delete, student_list

urlpatterns = [
path('', student_add_update, name='student_add_update'), 
path('<int:id>/', student_add_update, name='student_update'), 
path('delete/<int:id>/',student_delete,name='student_delete'),
path('list/',student_list, name='student_list') 
]
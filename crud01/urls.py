from django.urls import path
from . import views

app_name='crud01'

urlpatterns = [
    path('',views.task_list_and_create,name='crud_list'),
    path('update_task/<int:task_id>',views.update_task,name='update_task'),
]
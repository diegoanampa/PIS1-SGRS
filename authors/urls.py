from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('author/new/', views.author_create, name='author_create'),  # Ruta para crear un nuevo autor primero
    path('author/<str:pk>/', views.author_detail, name='author_detail'),
    path('author/<str:pk>/edit/', views.author_update, name='author_update'),
    path('author/<str:pk>/delete/', views.author_delete, name='author_delete'),
]

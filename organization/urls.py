from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(views.organization_list), name='organization_list'),
    path('new/', login_required(views.organization_create), name='organization_create'),
    path('<str:pk>/', login_required(views.organization_detail), name='organization_detail'),
    path('<str:pk>/edit/', login_required(views.organization_update), name='organization_update'),
    path('<str:pk>/delete/', login_required(views.organization_delete), name='organization_delete'),

]


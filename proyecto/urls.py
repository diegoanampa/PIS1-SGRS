from django.urls import path, include #la navegacion debe ser con el include para linkear organziaciones
from . import views
from django.contrib.auth.decorators import login_required

#app_name = 'proyecto'
urlpatterns = [
    path('<str:org_cod>/', login_required(views.proyecto_list), name='proyecto_list'),
    path('<str:org_cod>/create/', login_required(views.proyecto_create), name='proyecto_create'),
    path('<str:org_cod>/<str:pk>/', login_required(views.proyecto_detail), name='proyecto_detail'),
    path('<str:org_cod>/<str:pk>/update/', login_required(views.proyecto_update), name='proyecto_update'),
    path('<str:org_cod>/<str:pk>/delete/', login_required(views.proyecto_delete), name='proyecto_delete'),
    path('<str:org_cod>/<str:pk>/menuproyecto/',login_required(views.proyecto_menu), name='proyecto_menu'),
    path('<str:org_cod>/<str:pk>/menuproyecto/acta', login_required(views.proyecto_acta), name='proyecto_acta'),
    #path('<str:org_cod>/menuproyecto/acta', login_required(views.proyecto_acta), name='proyecto_acta'),
    path('<str:org_cod>/<str:pk>/menuproyecto/autores',login_required(views.proyecto_autores), name='proyecto_autores'),
    path('<str:org_cod>/<str:pk>/menuproyecto/autores/create',login_required(views.proyecto_autores_create), name='proyecto_autores_create'),
    # path('<str:org_cod>/<str:pk>/menuproyecto/autores/id_autor/detail',login_required(views.proyecto_autores_detail), name='proyecto_autores_detail'),
    # path('<str:org_cod>/<str:pk>/menuproyecto/autores/id_autor/update',login_required(views.proyecto_autores_update), name='proyecto_autores_update'),
    # path('<str:org_cod>/<str:pk>/menuproyecto/autores/id_autor/delete',login_required(views.proyecto_autores_delete), name='proyecto_autores_delete'),
    path('<str:org_cod>/<str:pk>/menuproyecto/menuplantillas', login_required(views.proyecto_menu_plantillas), name='proyecto_menu_plantillas'),

]


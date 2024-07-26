from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('role/create/', views.role_create, name='role_create'),
    path('role/list', views.role_list, name='role_list'),
    path('role/enconstruccion/', views.role_create, name='role_en_construccion'),
    path('role/<str:pk>/', views.role_detail, name='role_detail'),
    path('role/<str:pk>/update/', views.role_update, name='role_update'),
    path('role/<str:pk>/delete/', views.role_delete, name='role_delete'),
    
    
    # path('ruta para rol'),
    # path('ruta para rol create'),
    # path('ruta para rol update'),
    # path('ruta para rol delete'),
#EDUCCION
    # path('ruta para educcion'),
    path('<str:pro_cod>/educcion', login_required(views.educcion_list), name='educcion_list'),
    path('<str:pro_cod>/educcion/create', login_required(views.educcion_create), name='educcion_create'),
    path('<str:pro_cod>/educcion/<str:edu_cod>', login_required(views.educcion_detail), name='educcion_detail'),
    path('<str:pro_cod>/educcion/<str:edu_cod>/update/', login_required(views.educcion_update), name='educcion_update'),
    path('<str:pro_cod>/educcion/<str:edu_cod>/delete', login_required(views.educcion_delete), name='educcion_delete'),
    # path('ruta para educcion create'),
    # path('ruta para educcion update'),
    # path('ruta para educc on delete'),

#ILACION, IlacionForm
    path('<str:pro_cod>/ilacion', login_required(views.ilacion_list), name='ilacion_list'),
    path('<str:pro_cod>/ilacion/create', login_required(views.ilacion_create), name='ilacion_create'),
    path('<str:pro_cod>/ilacion/<str:ila_cod>', login_required(views.ilacion_detail), name='ilacion_detail'),
    path('<str:pro_cod>/ilacion/<str:ila_cod>/update/', login_required(views.ilacion_update), name='ilacion_update'),
    path('<str:pro_cod>/ilacion/<str:ila_cod>/delete', login_required(views.ilacion_delete), name='ilacion_delete'),

#ESPECIFICACION
    path('<str:pro_cod>/especificacion', login_required(views.especificacion_list), name='especificacion_list'),
    path('<str:pro_cod>/especificacion/create', login_required(views.especificacion_create), name='especificacion_create'),
    path('<str:pro_cod>/especificacion/<str:esp_cod>', login_required(views.especificacion_detail), name='especificacion_detail'),
    path('<str:pro_cod>/especificacion/<str:esp_cod>/update/', login_required(views.especificacion_update), name='especificacion_update'),
    path('<str:pro_cod>/especificacion/<str:esp_cod>/delete', login_required(views.especificacion_delete), name='especificacion_delete'),


#ENTREVISTAS

    path('<str:pro_cod>/entrevista', login_required(views.entrevista_list), name='entrevista_list'),
    path('<str:pro_cod>/entrevista/create', login_required(views.entrevista_create), name='entrevista_create'),
    path('<str:pro_cod>/entrevista/<str:entr_cod>', login_required(views.entrevista_detail), name='entrevista_detail'),
    path('<str:pro_cod>/entrevista/<str:entr_cod>/update/', login_required(views.entrevista_update), name='entrevista_update'),
    path('<str:pro_cod>/entrevista/<str:entr_cod>/delete', login_required(views.entrevista_delete), name='entrevista_delete'),

]

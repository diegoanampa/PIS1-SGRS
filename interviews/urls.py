from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import create_evidence, evidence_detail, evidence_delete, evidence_list

urlpatterns = [
    path('nueva-evidencia/', create_evidence, name='create_evidence'),
    path('evidencias/', evidence_list, name='evidence_list'),
    path('evidencias/<int:pk>/', evidence_detail, name='evidence_detail'),
    path('evidencias/<int:pk>/eliminar/', evidence_delete, name='evidence_delete'),
    
    # path('', 'interviews/pk/org_cod/', name=''),
    # path('', 'interviews/pk/org_cod/', name=''),
    # path('', 'interviews/pk/org_cod/', name=''),
    # path('', 'interviews/pk/org_cod/', name=''),
    # path('', 'interviews/pk/org_cod/', name=''),

    # path('', 'evidence/pk/org_cod/', name=''),
    # path('', 'evidence/pk/org_cod/', name=''),
    # path('', 'evidence/pk/org_cod/', name=''),
   
]


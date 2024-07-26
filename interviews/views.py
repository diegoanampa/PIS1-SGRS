from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import *
from .forms import InterviewForm, EvidenceForm

# Create your views here.


# ENTREVISTAS

# def proyecto_entrevista(request):
#     return render(request,'')

# def proyecto_entrevista_create(request):
#     return render(request,'')

# def proyecto_entrevista_detail(request):
#     return render(request,'')

# def proyecto_entrevista_update(request):
#     return render(request,'')

# def proyecto_entrevista_delete(request):
#     return render(request,'')


# EVIDENCIA

def create_evidence(request):
    if request.method == 'POST':
        form = EvidenceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('evidence_list')  # Asegúrate de que esta URL esté definida
    else:
        form = EvidenceForm()
    return render(request, 'evidence/create_evidence.html', {'form': form})

def evidence_detail(request, pk):
    evidence = get_object_or_404(Evidence, pk=pk)
    return render(request, 'evidence/evidence_detail.html', {'evidence': evidence})

def evidence_delete(request, pk):
    evidence = get_object_or_404(Evidence, pk=pk)
    if request.method == 'POST':
        evidence.delete()
        return redirect('evidence_list')
    return render(request, 'evidence/evidence_confirm_delete.html', {'evidence': evidence})

def evidence_list(request):
    evidences = Evidence.objects.all()
    return render(request, 'evidence/evidence_list.html', {'evidences': evidences})

# def proyecto_evidencia_create(request):
#     return render(request,'')
# def proyecto_evidencia_detail(request):
#     return render(request,'')
# def proyecto_evidencia_delete(request):
#     return render(request,'')





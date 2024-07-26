from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Proyecto
from organization.models import Organization
from .forms import ProyectoForm
from .forms import ActaAceptacionForm
from interviews.models import Artifact

def proyecto_list(request, org_cod):
    print("code recive: ", org_cod)
    organization = get_object_or_404(Organization, OrgCod=org_cod)
    proyectos = Proyecto.objects.filter(ProOrgCod=organization)
    #proyectos = Proyecto.objects.all()
    return render(request, 'proyecto/proyecto_list.html', {'proyectos': proyectos,'org_cod': org_cod,'organ': organization })

def proyecto_detail(request, org_cod, pk):
    proyecto = get_object_or_404(Proyecto, ProCod=pk)
    return render(request, 'proyecto/proyecto_detail.html', {'proyecto': proyecto,'org_cod': org_cod})

def proyecto_create(request, org_cod):
    organization = Organization.objects.get(OrgCod=org_cod)
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.ProOrgCod = organization
            proyecto.save()
            return redirect('proyecto_list', org_cod=org_cod)
    else:
        form = ProyectoForm()
    return render(request, 'proyecto/proyecto_form.html', {'form': form,'org_cod': org_cod })

def proyecto_update(request, org_cod, pk):
    proyecto = get_object_or_404(Proyecto, ProCod=pk)
    organization = Organization.objects.get(OrgCod=org_cod)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.ProOrgCod = organization
            return redirect('proyecto_list', org_cod=org_cod)
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyecto/proyecto_form.html', {'form': form,'org_cod': org_cod })

def proyecto_delete(request, org_cod, pk):
    proyecto = get_object_or_404(Proyecto, ProCod=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('proyecto_list', org_cod=org_cod)
    return render(request, 'proyecto/proyecto_confirm_delete.html', {'proyecto': proyecto,'org_cod': org_cod })

def proyecto_menu(request, org_cod, pk):
    # proyecto =Artifact.objects.all()
    proyecto = get_object_or_404(Proyecto,ProCod=pk)
    organization = get_object_or_404(Organization,OrgCod=org_cod)
    # print("dsadasd", proyecto)
    # logica
    return render(request,'proyecto/proyecto_menu.html',{'org':organization,'proyecto':proyecto})

# ACTA
def proyecto_acta(request,org_cod, pk):
    #logica
    
    proyecto = get_object_or_404(Proyecto, pk=pk)
    
    if request.method == 'POST':
        form = ActaAceptacionForm(request.POST, request.FILES)
        if form.is_valid():
            acta = form.save(commit=False)
            acta.ActAceCod = proyecto
            acta.save()
            return redirect('proyecto_acta', org_cod=org_cod, pk=pk)
    else:
        form = ActaAceptacionForm(initial={'ActAceCod': proyecto})
        
    return render(request, 'proyecto/proyecto_acta.html', {'form': form, 'proyecto': proyecto})

# AUTORES

def proyecto_autores(request,org_cod, pk):
    #logica
    return render(request,'proyecto/proyecto_autores.html')

def proyecto_autores_create(request,org_cod,pk):
    return render(request,'proyecto/proyecto_autores_create.html')

# def proyecto_autores_detail(request,org_cod,pk,id_aut):
#     return render(request,'proyecto/proyecto_autores_detail.html')


# def proyecto_autores_update(request,org_cod,pk,id_aut):
#     return render(request,'proyecto/proyecto_autores_update.html')


# def proyecto_autores_delete(request,org_cod,pk,id_aut):
#     return render(request,'proyecto/proyecto_autores_delete.html')

# PLANTILLAS

def proyecto_menu_plantillas(request, org_cod, pk):
    # proyecto =Artifact.objects.all()
    proyecto = get_object_or_404(Proyecto,ProCod=pk)
    organization = get_object_or_404(Organization,OrgCod=org_cod)
    # print("dsadasd", proyecto)
    return render(request,'proyecto/proyecto_menu_plantillas.html',{'org':organization,'proyecto':proyecto})


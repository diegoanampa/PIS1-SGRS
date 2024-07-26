from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import *

from .forms import LoginForm
from .models import Role
from .forms import LoginForm, EduccionForm, RoleForm, EntrevistaForm, IlacionForm, EspecificacionForm

from proyecto.models import Proyecto
# ROL
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role/role_list.html', {'roles': roles})

def role_detail(request, pk):
    role = get_object_or_404(Role, RolCod=pk)
    return render(request, 'role/role_detail.html', {'role': role})

def role_create(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'role/role_form.html', {'form': form})

def role_update(request, pk):
    role = get_object_or_404(Role, RolCod=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'role/role_form.html', {'form': form})

def role_delete(request, pk):
    role = get_object_or_404(Role, RolCod=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('role_list')
    return render(request, 'role/role_confirm_delete.html', {'role': role})

def role_en_construccion(request):
    
    return render(request, 'role/role_en_constrccion.html')



# EDUCCION

def educcion_list(request, pro_cod):
    project = get_object_or_404(Proyecto, ProCod=pro_cod)
    educciones = Educcion.objects.filter(EduProCod=project)

    return render(request, 'educcion/educcion_list.html', {'educciones': educciones,'pro_cod': pro_cod,'project': project })

def educcion_detail(request, pro_cod, edu_cod):
    educcion = get_object_or_404(Educcion, EduCod=edu_cod)
    ilaciones = educcion.ilaciones.all()
    print("ilaciones, ", ilaciones)
    return render(request, 'educcion/educcion_detail.html', {'educcion': educcion,'pro_cod': pro_cod,'ilaciones': ilaciones })


def educcion_create(request, pro_cod):
    projecto = Proyecto.objects.get(ProCod=pro_cod)
    author = Author.objects.first()
    print("autor", author)
    if request.method == 'POST':
        form = EduccionForm(request.POST)
        if form.is_valid():
            print("entrando a valid")
            educcion = form.save(commit=False)
            educcion.EduProCod = projecto
            educcion.EduAutCod = author
            educcion.save()
            form.save_m2m()
            return redirect('educcion_list', pro_cod=pro_cod)
    else:
        print("entrando a else")
        form = EduccionForm()
    return render(request, 'educcion/educcion_form.html', {'form': form,'pro_cod': pro_cod })

def educcion_update(request, pro_cod, edu_cod):
    project = get_object_or_404(Proyecto, ProCod=pro_cod)
    print("educcion: ", edu_cod)
    educcion = Educcion.objects.get(EduCod=edu_cod)
    if request.method == 'POST':
        form = EduccionForm(request.POST, instance=educcion)
        if form.is_valid():
            educcion = form.save(commit=False)
            educcion.EduProCod = project
            educcion.save()
            form.save_m2m()
            return redirect('educcion_list', pro_cod=pro_cod)
    else:
        form = EduccionForm(instance=educcion)
    return render(request, 'educcion/educcion_form.html', {'form': form,'pro_cod': pro_cod })

def educcion_delete(request, pro_cod, edu_cod):
    educcion = get_object_or_404(Educcion, EduCod=edu_cod)
    if request.method == 'POST':
        educcion.delete()
        return redirect('educcion_list', pro_cod=pro_cod)
    return render(request, 'educcion/educcion_confirm_delete.html', {'educcion': educcion,'pro_cod': pro_cod })


#ENTREVISTAS

def entrevista_list(request, pro_cod):
    project = get_object_or_404(Proyecto, ProCod=pro_cod)
    entrevistas = Entrevista.objects.filter(EntrProCod=project)

    return render(request, 'entrevista/entrevista_list.html', {'entrevistas': entrevistas,'pro_cod': pro_cod,'project': project })

def entrevista_detail(request, pro_cod, entr_cod):
    entrevista = get_object_or_404(Entrevista, EntrCod=entr_cod)
    return render(request, 'entrevista/entrevista_detail.html', {'entrevista': entrevista,'pro_cod': pro_cod})


def entrevista_create(request, pro_cod):
    projecto = Proyecto.objects.get(ProCod=pro_cod)
    author = Author.objects.first()
    print("autor", author)
    if request.method == 'POST':
        form = EntrevistaForm(request.POST)
        if form.is_valid():
            print("entrando a valid")
            entrevista = form.save(commit=False)
            entrevista.EntrProCod = projecto
            entrevista.EntrAutCod = author
            entrevista.save()
            return redirect('entrevista_list', pro_cod=pro_cod)
    else:
        print("entrando a else")
        form = EntrevistaForm()
    return render(request, 'entrevista/entrevista_form.html', {'form': form,'pro_cod': pro_cod })

def entrevista_update(request, pro_cod, entr_cod):
    project = get_object_or_404(Proyecto, ProCod=pro_cod)
    print("entrevista: ", entr_cod)
    entrevista = Entrevista.objects.get(EntrCod=entr_cod)
    if request.method == 'POST':
        form = EntrevistaForm(request.POST, instance=entrevista)
        if form.is_valid():
            entrevista = form.save(commit=False)
            entrevista.EntrProCod = project
            return redirect('entrevista_list', pro_cod=pro_cod)
    else:
        form = EntrevistaForm(instance=entrevista)
    return render(request, 'entrevista/entrevista_form.html', {'form': form,'pro_cod': pro_cod })

def entrevista_delete(request, pro_cod, entr_cod):
    entrevista = get_object_or_404(Entrevista, EntrCod=entr_cod)
    if request.method == 'POST':
        entrevista.delete()
        return redirect('entrevista_list', pro_cod=pro_cod)
    return render(request, 'entrevista/entrevista_confirm_delete.html', {'entrevista': entrevista,'pro_cod': pro_cod })

#ILACION
def ilacion_list(request, pro_cod):
    project = get_object_or_404(Proyecto, ProCod=pro_cod)
    ilaciones = Ilacion.objects.filter(IlaProCod=project)

    return render(request, 'ilacion/ilacion_list.html', {'ilaciones': ilaciones,'pro_cod': pro_cod,'project': project })

def ilacion_detail(request, pro_cod, ila_cod):
    ilacion = get_object_or_404(Ilacion, IlaCod=ila_cod)
    print("ilacion: ", ilacion.IlaEduCod)
    return render(request, 'ilacion/ilacion_detail.html', {'ilacion': ilacion,'pro_cod': pro_cod})


def ilacion_create(request, pro_cod):
    projecto = Proyecto.objects.get(ProCod=pro_cod)
    author = Author.objects.first()
    print("autor", author)
    if request.method == 'POST':
        form = IlacionForm(request.POST)
        if form.is_valid():
            print("entrando a valid")
            ilacion = form.save(commit=False)
            ilacion.IlaProCod = projecto
            ilacion.IlaAutPlanCod = author
            ilacion.save()
            return redirect('ilacion_list', pro_cod=pro_cod)
    else:
        print("entrando a else")
        form = IlacionForm()
    return render(request, 'ilacion/ilacion_form.html', {'form': form,'pro_cod': pro_cod })
def ilacion_update(request, pro_cod, ila_cod):
    project = get_object_or_404(Proyecto, ProCod=pro_cod)
    print("ilacion: ", ila_cod)
    ilacion = Ilacion.objects.get(IlaCod=ila_cod)
    if request.method == 'POST':
        form = IlacionForm(request.POST, instance=ilacion)
        if form.is_valid():
            print("Form data:", form.cleaned_data)

            ilacion = form.save(commit=False)
            ilacion.IlaProCod = project
            print("Before save:", ilacion.IlaEduCod)

            ilacion.save()
            print("After save:", Ilacion.objects.get(IlaCod=ila_cod).IlaEduCod)
            return redirect('ilacion_list', pro_cod=pro_cod)
    else:
        form = IlacionForm(instance=ilacion)
    return render(request, 'ilacion/ilacion_form.html', {'form': form,'pro_cod': pro_cod })

def ilacion_delete(request, pro_cod, ila_cod):
    ilacion = get_object_or_404(Ilacion, IlaCod=ila_cod)
    if request.method == 'POST':
        ilacion.delete()
        return redirect('ilacion_list', pro_cod=pro_cod)
    return render(request, 'ilacion/ilacion_confirm_delete.html', {'ilacion': ilacion,'pro_cod': pro_cod })


#ESPECIFICACION

def especificacion_list(request, pro_cod):
    project = get_object_or_404(Proyecto, ProCod=pro_cod)
    especificaciones = Especificacion.objects.filter(EspProCod=project)

    return render(request, 'especificacion/especificacion_list.html', {'especificaciones': especificaciones,'pro_cod': pro_cod,'project': project })

def especificacion_detail(request, pro_cod, esp_cod):
    especificacion = get_object_or_404(Especificacion, EspCod=esp_cod)
    #ilaciones = especificacion.ilaciones.all()
    #print("ilaciones, ", ilaciones)
    return render(request, 'especificacion/especificacion_detail.html', {'especificacion': especificacion,'pro_cod': pro_cod })


def especificacion_create(request, pro_cod):
    projecto = Proyecto.objects.get(ProCod=pro_cod)
    author = Author.objects.first()
    print("autor", author)
    if request.method == 'POST':
        form = EspecificacionForm(request.POST)
        if form.is_valid():
            print("entrando a valid")
            especificacion = form.save(commit=False)
            especificacion.EspProCod = projecto
            especificacion.EspAutPlanCod = author
            especificacion.save()
            return redirect('especificacion_list', pro_cod=pro_cod)
    else:
        print("entrando a else")
        form = EspecificacionForm()
    return render(request, 'especificacion/especificacion_form.html', {'form': form,'pro_cod': pro_cod })

def especificacion_update(request, pro_cod, esp_cod):
    project = get_object_or_404(Proyecto, ProCod=pro_cod)
    print("especificacion: ", esp_cod)
    especificacion = Especificacion.objects.get(EspCod=esp_cod)
    if request.method == 'POST':
        form = EspecificacionForm(request.POST, instance=especificacion)
        if form.is_valid():
            especificacion = form.save(commit=False)
            especificacion.EspProCod = project
            especificacion.save()
            return redirect('especificacion_list', pro_cod=pro_cod)
    else:
        form = EspecificacionForm(instance=especificacion)
    return render(request, 'especificacion/especificacion_form.html', {'form': form,'pro_cod': pro_cod })

def especificacion_delete(request, pro_cod, esp_cod):
    especificacion = get_object_or_404(Especificacion, EspCod=esp_cod)
    if request.method == 'POST':
        especificacion.delete()
        return redirect('especificacion_list', pro_cod=pro_cod)
    return render(request, 'especificacion/especificacion_confirm_delete.html', {'especificacion': especificacion,'pro_cod': pro_cod })





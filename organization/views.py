from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Organization
from .forms import OrganizationForm

def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organization/organization_list.html', {'organizations': organizations})

def organization_detail(request, pk):
    organization = get_object_or_404(Organization, OrgCod=pk)
    return render(request, 'organization/organization_detail.html', {'organization': organization})

def organization_create(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization_list')
    else:
        form = OrganizationForm()
    return render(request, 'organization/organization_form.html', {'form': form})

def organization_update(request, pk):
    organization = get_object_or_404(Organization, OrgCod=pk)
    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('organization_list')
    else:
        form = OrganizationForm(instance=organization)
    return render(request, 'organization/organization_form.html', {'form': form})

def organization_delete(request, pk):
    organization = get_object_or_404(Organization, OrgCod=pk)
    if request.method == 'POST':
        organization.delete()
        return redirect('organization_list')
    return render(request, 'organization/organization_confirm_delete.html', {'organization': organization})


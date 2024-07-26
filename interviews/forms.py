from django import forms
from .models import Interview, Evidence

class InterviewForm(forms.ModelForm):
    OrgFecCre = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )
    OrgFecMod = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = Interview
        fields = '__all__'  # Todos los campos del modelo


class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = ['EviCod', 'EviNom', 'EviEntCod', 'EviFec', 'EviArc', 'EviCatEviCod', 'EviArtCod']
        widgets = {
            'EviFec': forms.DateInput(attrs={'type': 'date'}),
        }
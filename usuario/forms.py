from django import forms
from .models import Role, Educcion, Entrevista, Ilacion, Especificacion

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import Role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['RolCod', 'RolNom', 'RolCom', 'RolOrgCod']
        labels = {
            'RolCod': 'Código del Rol',
            'RolNom': 'Nombre del Rol',
            'RolCom': 'Comentarios',
            'RolOrgCod': 'Código de Organización',
        }
        widgets = {
            'RolOrgCod': forms.Select(), 
        }

class EduccionForm(forms.ModelForm):
    ilaciones = forms.ModelMultipleChoiceField(
        queryset=Ilacion.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Ilaciones'
    )

    class Meta:
        model = Educcion
        fields = '__all__'
        exclude = ['EduProCod','EduAutCod']

    def __init__(self, *args, **kwargs):
        super(EduccionForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['ilaciones'].initial = self.instance.ilaciones.all()

    def save(self, commit=True):
        instance = super(EduccionForm, self).save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance

    def save_m2m(self):
        self.instance.ilaciones.set(self.cleaned_data['ilaciones'])

class IlacionForm(forms.ModelForm):
    class Meta:
        model = Ilacion
        fields = '__all__'
        exclude = ['IlaProCod','IlaAutPlanCod']

class EspecificacionForm(forms.ModelForm):
    class Meta:
        model = Especificacion
        fields = '__all__'
        exclude = ['EspProCod','EspAutPlanCod']

class EntrevistaForm(forms.ModelForm):
    class Meta:
        model = Entrevista
        fields = '__all__'
        exclude = ['EntrProCod','EntrAutCod']

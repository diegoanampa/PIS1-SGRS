from django import forms
from .models import Proyecto
from .models import ActaAcceptation

class ProyectoForm(forms.ModelForm):
    ProFecCre = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )
    ProFecMod = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = Proyecto
        #fields = '__all__'  # Todos los campos del modelo
        exclude = ['ProOrgCod']

    def clean_ProCod(self):
        pro_cod = self.cleaned_data.get('ProCod')
        # Validación personalizada para ProCod
        if not pro_cod.isalnum():
            raise forms.ValidationError('El código del proyecto debe ser alfanumérico.')
        return pro_cod

    def clean_ProVer(self):
        pro_ver = self.cleaned_data.get('ProVer')
        # Validación personalizada para ProVer
        if not pro_ver:
            raise forms.ValidationError('La versión del proyecto es obligatorio.')
        return pro_ver

    def clean_ProNom(self):
        pro_nom = self.cleaned_data.get('ProNom')
        # Validación personalizada para ProNom
        if not pro_nom:
            raise forms.ValidationError('El nombre del proyecto es obligatorio.')
        return pro_nom

    def clean_ProEst(self):
        pro_est = self.cleaned_data.get('ProEst')
        # Validación personalizada para ProEst
        valid_states = ['En progreso','Concluido']
        if pro_est not in valid_states:
            raise forms.ValidationError(
                'El estado del proyecto debe ser uno de los siguientes: En progreso, Concluido.'
            )
        return pro_est

    def clean(self):
        cleaned_data = super().clean()
        pro_fec_cre = cleaned_data.get('ProFecCre')
        pro_fec_mod = cleaned_data.get('ProFecMod')

        # Validación general
        if pro_fec_cre and pro_fec_mod and pro_fec_cre > pro_fec_mod:
            self.add_error('ProFecCre', 'La fecha de creación no puede ser posterior a la fecha de modificación.')
            self.add_error('ProFecMod', 'La fecha de modificación no puede ser anterior a la fecha de creación.')

        return cleaned_data

class ActaAceptacionForm(forms.ModelForm):
    class Meta:
        model = ActaAcceptation
        fields = ['ActAceCod', 'ActAceArc']

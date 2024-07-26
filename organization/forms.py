from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    OrgFecCre = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )
    OrgFecMod = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = Organization
        fields = '__all__'  # Todos los campos del modelo


    def clean_OrgCod(self):
        pro_cod = self.cleaned_data.get('OrgCod')
        # Validación personalizada para OrgCod
        if not pro_cod.isalnum():
            raise forms.ValidationError('El código del proyecto debe ser alfanumérico.')
        return pro_cod

    def clean_OrgVer(self):
        pro_ver = self.cleaned_data.get('OrgVer')
        # Validación personalizada para OrgVer
        if not pro_ver:
            raise forms.ValidationError('La versión del proyecto es obligatorio.')
        return pro_ver

    def clean_OrgNom(self):
        pro_nom = self.cleaned_data.get('OrgNom')
        # Validación personalizada para OrgNom
        if not pro_nom:
            raise forms.ValidationError('El nombre del proyecto es obligatorio.')
        return pro_nom

    def clean_OrgEst(self):
        pro_est = self.cleaned_data.get('OrgEst')
        # Validación personalizada para OrgEst
        valid_states = ['En progreso','Concluido']
        if pro_est not in valid_states:
            raise forms.ValidationError(
                'El estado del proyecto debe ser uno de los siguientes: En progreso, Concluido.'
            )
        return pro_est

    def clean(self):
        cleaned_data = super().clean()
        pro_fec_cre = cleaned_data.get('OrgFecCre')
        pro_fec_mod = cleaned_data.get('OrgFecMod')

        # Validación general
        if pro_fec_cre and pro_fec_mod and pro_fec_cre > pro_fec_mod:
            self.add_error('OrgFecCre', 'La fecha de creación no puede ser posterior a la fecha de modificación.')
            self.add_error('OrgFecMod', 'La fecha de modificación no puede ser anterior a la fecha de creación.')

        return cleaned_data

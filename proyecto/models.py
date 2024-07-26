from django.db import models
from organization.models import Organization

# Create your models here.

class Proyecto(models.Model):
    ProCod = models.CharField(max_length=50, primary_key=True)  # Codigo
    ProVer = models.CharField(max_length=50)  # Version
    ProNom = models.CharField(max_length=255)  # Nombre
    ProFecCre = models.DateField()  # FechaCreacion
    ProFecMod = models.DateField()  # FechaModificacion
    ProEst = models.CharField(max_length=50)  # Estado
    ProCom = models.TextField(blank=True)  # Comentario campo opcional
    ProOrgCod = models.ForeignKey(Organization, on_delete=models.CASCADE)
    ProCodModPlan = models.CharField(max_length=50)  # Codigo de Modificacion Plantillas

    def __str__(self):
        return self.ProNom 

class ActaAcceptation(models.Model):
    ActAceCod = models.OneToOneField(Proyecto, primary_key=True, on_delete=models.CASCADE)
    ActAceArc = models.FileField(upload_to='actas/')  # Aquí defines la ruta donde se guardarán los archivos

    def __str__(self):
        return str(self.ActAceCod)

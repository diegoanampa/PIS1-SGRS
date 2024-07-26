from django.db import models

# Create your models here.
class Artifact(models.Model):
    ArtCod = models.CharField(max_length=50, primary_key=True)
    ArtNom = models.CharField(max_length=255)
    ArtNem = models.CharField(max_length=255)

    def __str__(self):
        return self.ArtNom

class OrganizationType(models.Model):
    TipOrgCod = models.CharField(max_length=50, primary_key=True)  # Type Code
    TipOrgNom = models.CharField(max_length=255)  # Name
    TipOrgDes = models.TextField()  # Description

    def __str__(self):
        return self.TipOrgNom

class Organization(models.Model):
    OrgCod = models.CharField(max_length=50, primary_key=True)  # Codigo
    OrgVer = models.CharField(max_length=50)  # Version
    OrgNom = models.CharField(max_length=255)  # Nombre
    OrgFecCre = models.DateField()  # FechaCreacion
    OrgFecMod = models.DateField()  # FechaModificacion
    OrgCom = models.TextField(blank=True)  # Comentario campo opcional
    OrgCodModPlan = models.CharField(max_length=50)  # Codigo de Modificacion Plantillas
    OrgTipOrgCod = models.ForeignKey(OrganizationType, on_delete=models.CASCADE)  # Foreign key to OrganizationType
    OrgAutCod = models.CharField(max_length=50)
    OrgDir = models.CharField(max_length=255)
    OrgTel = models.IntegerField()
    OrgRepLeg = models.CharField(max_length=255)
    OrgTelRepLeg = models.IntegerField()
    OrgRuc = models.IntegerField()
    OrgContact = models.CharField(max_length=255)
    OrgTelCon = models.CharField(max_length=50)
    OrgCom = models.CharField(max_length=255)
    OrgArtCod = models.ForeignKey(Artifact, on_delete=models.CASCADE)

    def __str__(self):
        return self.OrgNom 

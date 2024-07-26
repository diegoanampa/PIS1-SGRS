from django.db import models
from organization.models import Artifact
from usuario.models import Author
from proyecto.models import Proyecto
# Create your models here.

class CategoryEvidence(models.Model):
    CatEviCod = models.CharField(max_length=50, primary_key=True)
    CatEviNom = models.CharField(max_length=255)

    def __str__(self):
        return self.CatEviNom

class Interview(models.Model):
    EntCod = models.CharField(max_length=50, primary_key=True)
    EntVer = models.FloatField()
    EntFec = models.DateField()
    EntAutCod = models.ForeignKey(Author, on_delete=models.CASCADE)
    EntNomEnt = models.CharField(max_length=255)
    EntCarEnt = models.CharField(max_length=255)
    EntHorIni = models.TimeField()
    EntHorFin = models.TimeField()
    EntDur = models.IntegerField()
    EntObsTie = models.CharField(max_length=255)
    EntObs = models.TextField()
    EntProCod = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    EntArtCod = models.ForeignKey(Artifact, on_delete=models.CASCADE)

    def __str__(self):
        return self.EntNomEnt

class Schedule(models.Model):
    AgeCod = models.CharField(max_length=50, primary_key=True)
    AgeEntCod = models.ForeignKey(Interview, on_delete=models.CASCADE)
    AgeTex = models.TextField()
    def __str__(self):
        return self.AgeCod

class Conclusion(models.Model):
    ConCod = models.CharField(max_length=50, primary_key=True)
    ConEntCod = models.ForeignKey(Interview, on_delete=models.CASCADE)
    ConTex = models.TextField()
    def __str__(self):
        return self.ConCod

class Evidence(models.Model):
    EviCod = models.CharField(max_length=50, primary_key=True)
    EviNom = models.CharField(max_length=255)
    EviEntCod = models.ForeignKey(Interview, on_delete=models.CASCADE)
    EviFec = models.DateField()
    EviArc = models.FileField(upload_to='evidences/')
    EviCatEviCod = models.ForeignKey(CategoryEvidence, on_delete=models.CASCADE)
    EviArtCod = models.ForeignKey(Artifact, on_delete=models.CASCADE)

    def __str__(self):
        return self.EviNom


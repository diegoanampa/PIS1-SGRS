from django.db import models
from organization.models import Organization
from organization.models import Artifact
from proyecto.models import Proyecto

# Create your models here.

class State(models.Model):
    EstCod = models.CharField(primary_key=True, max_length=100)
    EstNom = models.CharField(max_length=255, verbose_name='Nombre')
    EstDescrip = models.CharField(max_length=255, verbose_name='Descripción')

    def __str__(self):
        return self.EstNom


class Author(models.Model):
    AutCod = models.CharField(primary_key=True, max_length=50)
    AutVer = models.FloatField()
    AutFecIng = models.DateField()
    AutAli = models.CharField(max_length=255)
    AutOrgCod = models.ForeignKey(Organization, on_delete=models.CASCADE)
    AutEstCod = models.ForeignKey(State, on_delete=models.CASCADE)
    AutCom = models.CharField(max_length=255)
    AutApeMat = models.CharField(max_length=255)
    AutApePat = models.CharField(max_length=255)
    AutNom = models.CharField(max_length=255)
    AutCon = models.CharField(max_length=255)
    AutTel = models.IntegerField()
    AutDNI = models.IntegerField()

    def _str_(self):
        return self.AutCod

class ModificationArtifact(models.Model):
    ModArtCod = models.CharField(primary_key=True, max_length=50)
    ModArtFecMod = models.DateField()
    ModArtCom = models.CharField(max_length=255)
    ModArtTipPlan = models.CharField(max_length=255)
    ModArtArtCod = models.ForeignKey(Artifact, on_delete=models.CASCADE)
    ModArtVer = models.FloatField()
    ModArtAutCod = models.ForeignKey(Author, on_delete=models.CASCADE)

    def _str_(self):
        return self.ModArtCod

class OperationArtifact(models.Model):
    OpeArtCod = models.CharField(primary_key=True, max_length=50)
    OpeArtNom = models.CharField(max_length=255)
    OperArtArtCod = models.ForeignKey(Artifact, on_delete=models.CASCADE)

    def _str_(self):
        return self.OpeArtCod



class Role(models.Model):
    RolCod = models.CharField(primary_key=True, max_length=50)
    RolNom = models.CharField(max_length=255)
    RolFecCre = models.DateField(auto_now_add=True)
    RolCom = models.CharField(max_length=255)
    RolOrgCod = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def _str_(self):
        return self.RolCod

class AuthorRole(models.Model):
    AutRolCod = models.CharField(primary_key=True, max_length=50)
    AutRolAutCod = models.ForeignKey(Author, on_delete=models.CASCADE)
    AutRolRolCod = models.ForeignKey(Role, on_delete=models.CASCADE)

    def _str_(self):
        return self.AutRolCod

class AuthorPermission(models.Model):
    PerAutCod = models.CharField(primary_key=True, max_length=50)
    PerAutOpeArtCod = models.ForeignKey(OperationArtifact, on_delete=models.CASCADE)
    PerAutAutCod = models.ForeignKey(Author, on_delete=models.CASCADE)

    def _str_(self):
        return self.PerAutCod

class Report(models.Model):
    RepCod = models.CharField(primary_key=True, max_length=50)
    RepFec = models.DateField()
    RepProCod = models.CharField(max_length=255)
    RepVer = models.FloatField()
    RepArtCod = models.ForeignKey(Artifact, on_delete=models.CASCADE)
    RepAutCod = models.ForeignKey(Author, on_delete=models.CASCADE)
    RepFil = models.FileField(upload_to='reports/')

    def _str_(self):
        return self.RepCod

class TypeActor(models.Model):
    TipActCod = models.CharField(primary_key=True, max_length=50)
    TipActNomAct = models.CharField(max_length=255)

    def _str_(self):
        return self.TipActCod



class RoleActor(models.Model):
    RolActCod = models.CharField(primary_key=True, max_length=50)
    RolActNom = models.CharField(max_length=255)

    def _str_(self):
        return self.RolActCod

  

class Actor(models.Model):
    ActCod = models.CharField(primary_key=True, max_length=50)
    ActVer = models.FloatField()
    ActFecCrea = models.DateField(auto_now_add=True)
    ActFecMod = models.DateField()
    ActAutPlaCod = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='autores_placod')
    ActEstCod = models.ForeignKey(State, on_delete=models.CASCADE)
    ActCom = models.CharField(max_length=255)
    ActProCod = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    ActTipActCod = models.ForeignKey(TypeActor, on_delete=models.CASCADE)
    ActArtCod = models.ForeignKey(Artifact, on_delete=models.CASCADE)
    ActRolActCod = models.ForeignKey(RoleActor, on_delete=models.CASCADE)

    def _str_(self):
        return self.ActCod

class Expert(models.Model):
    ExpCod = models.CharField(primary_key=True, max_length=50)
    ExpVer = models.FloatField()
    ExpFecCre = models.DateField(auto_now_add=True)
    ExpFecMod = models.DateField()
    ExpApePat = models.CharField(max_length=255)
    ExpApeMat = models.CharField(max_length=255)
    ExpNom = models.CharField(max_length=255)
    ExpExp = models.CharField(max_length=255)
    ExpProCod = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    ExpAutPlaCod = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='experto_autor_plan')
    ExpCom = models.CharField(max_length=255)
    ExpArtCod = models.ForeignKey(Artifact, on_delete=models.CASCADE)
    ExpEstaCod = models.ForeignKey(State, on_delete=models.CASCADE)

    def _str_(self):
        return self.ExpCod



class Font(models.Model):
    FueCod = models.CharField(primary_key=True, max_length=50)
    FueVer = models.FloatField()
    FueFecCre = models.DateField(auto_now_add=True) 
    FueFecMod = models.DateField()
    FueAutPlanCod = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='fuente_autor_plan')
    FueEstCod = models.ForeignKey(State, on_delete=models.CASCADE)
    FueCom = models.CharField(max_length=255)
    FueProCod = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def _str_(self):
        return self.FueCod

class Educcion(models.Model):
    EduCod = models.CharField(primary_key=True, max_length=50)
    EduNom = models.CharField(max_length=50, null=True, blank=True)
    EduVer = models.FloatField()
    EduFecCre = models.DateField(auto_now_add=True)
    EduFecMod = models.DateField()
    EduEstCod = models.ForeignKey(State, on_delete=models.CASCADE)
    #EduIlaCod = models.ForeignKey(Ilacion, on_delete=models.CASCADE)
    EduCom = models.CharField(max_length=255)
    EduProCod = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    EduAutCod = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    EduFueCod = models.ForeignKey(Font, null=True, blank=True, on_delete=models.SET_NULL)
    EduExpCod = models.ForeignKey(Expert, on_delete=models.CASCADE)
    EduActCod = models.ForeignKey(Actor, null=True, blank=True, on_delete=models.SET_NULL)
    EduArtCod = models.ForeignKey(Artifact, null=True, blank=True, on_delete=models.SET_NULL)

    def str(self):
        return self.EduCod

class Ilacion(models.Model):
    IlaCod = models.CharField(max_length=50, primary_key=True)
    IlaNom = models.CharField(max_length=50, null=True, blank=True)
    IlaVer = models.FloatField()
    IlaFecCre = models.DateField(auto_now_add=True)
    IlaFecMod = models.DateField()
    IlaEstCod = models.ForeignKey(State, null=True, blank=True, on_delete=models.SET_NULL)
    #IlaNivPriCod = models.ForeignKey(NivelPrioridad, null=True, blank=True, on_delete=models.SET_NULL)
    IlaEduCod = models.ForeignKey(Educcion, related_name='ilaciones', on_delete=models.CASCADE)
    #IlaEspCod = models.ForeignKey(Especificacion, null=True, blank=True, on_delete=models.SET_NULL)
    IlaCom = models.CharField(max_length=255, blank=True)
    IlaProCod = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.SET_NULL)
    IlaAutPlanCod = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    IlaFueCod = models.ForeignKey(Font, null=True, blank=True, on_delete=models.SET_NULL)
    IlaExpCod = models.ForeignKey(Expert, null=True, blank=True, on_delete=models.SET_NULL)
    IlaActCod = models.ForeignKey(Actor, null=True, blank=True, on_delete=models.SET_NULL)
    IlaArtCod = models.ForeignKey(Artifact, null=True, blank=True, on_delete=models.SET_NULL)

    def _str_(self):
        return self.IlaCod

class Especificacion(models.Model):
    EspCod = models.CharField(max_length=50, primary_key=True)
    EspNom = models.CharField(max_length=50, null=True, blank=True)
    EspVer = models.FloatField()
    EspFecCre = models.DateField(auto_now_add=True)
    EspFecMod = models.DateField()
    EspEstCod = models.ForeignKey(State, null=True, blank=True, on_delete=models.SET_NULL)
    EspIlaCod = models.OneToOneField(Ilacion, null=True, blank=True, on_delete=models.CASCADE, related_name='especificacion')
    #EspNivPriCod = models.ForeignKey(NivelPrioridad, null=True, blank=True, on_delete=models.SET_NULL)
    EspCom = models.CharField(max_length=255, blank=True)
    EspProCod = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.SET_NULL)
    EspAutPlanCod = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    EspFueCod = models.ForeignKey(Font, null=True, blank=True, on_delete=models.SET_NULL)
    EspExpCod = models.ForeignKey(Expert, null=True, blank=True, on_delete=models.SET_NULL)
    EspActCod = models.ForeignKey(Actor, null=True, blank=True, on_delete=models.SET_NULL)
    EspArtCod = models.ForeignKey(Artifact, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.EspCod

class Entrevista(models.Model):
    EntrCod = models.CharField(primary_key=True, max_length=50)
    EntrVer = models.FloatField()
    EntrAutCod = models.ForeignKey(Author, on_delete=models.CASCADE)
    EntrFecCre = models.DateField(auto_now_add=True)
    EntrFecMod = models.DateField()
    EntrEstCod = models.ForeignKey(State, on_delete=models.CASCADE)
    EntrNomPer = models.CharField(max_length=50)
    EntrCargPer = models.CharField(max_length=50)
    EntrCom = models.CharField(max_length=255)
    EntrProCod = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    EntrFueCod = models.ForeignKey(Font, on_delete=models.CASCADE)
    EntrExpCod = models.ForeignKey(Expert, on_delete=models.CASCADE)
    EntrActCod = models.ForeignKey(Actor, on_delete=models.CASCADE)
    EntrArtCod = models.ForeignKey(Artifact, on_delete=models.CASCADE)

    def _str_(self):
        return self.EntrCod

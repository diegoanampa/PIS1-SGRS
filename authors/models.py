from django.db import models

class Author(models.Model):
    AutCod = models.CharField(max_length=255, primary_key=True)
    AutVer = models.CharField(max_length=255)
    AutFecIng = models.DateField()
    AutAli = models.CharField(max_length=255)
    AutCom = models.CharField(max_length=255)
    AutApeMat = models.CharField(max_length=255)
    AutApePat = models.CharField(max_length=255)
    AutNom = models.CharField(max_length=255)
    AutCon = models.CharField(max_length=255)
    AutTel = models.CharField(max_length=255)
    AutDNI = models.CharField(max_length=255)
    AutOrgCod_id = models.CharField(max_length=255)
    AutEstCod_id = models.CharField(max_length=255)

    def __str__(self):
        return self.AutNom

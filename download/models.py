from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Matiére(models.Model):
  matiére = models.CharField(max_length=200)
  def __str__(self):
        return self.matiére
class Professeur(models.Model):
  name = models.CharField(max_length=200)
  matiére = models.ForeignKey(Matiére, on_delete=models.SET_NULL, null=True, blank=True)
  def __str__(self):
        return self.name

class Etudiant(models.Model): 
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=2000)
  téléphone = models.CharField(max_length=16)

  def __str__(self):
        return self.name
  
    
class Cour(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.SET_NULL, null=True, blank=True)
    document = models.FileField()
    cour = models.CharField(max_length=200)
    partie = models.CharField(max_length=200,null=False,blank=False)
    def __str__(self):
        return self.cour

    @property
    def docFILE(self):
           try:
               url = self.document.url
           except:
               url = ''
           return url


class Exercice(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.SET_NULL, null=True, blank=True)
    document = models.FileField()
    exercice = models.CharField(max_length=200)
    def __str__(self):
        return self.exercice
    @property
    def docFILE1(self):

           try:
               url = self.document.url
           except:
               url = ''
           return url

class Corrigé(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.SET_NULL, null=True, blank=True)
    document = models.FileField()
    correction_name = models.CharField(max_length=200)
    def __str__(self):
        return self.correction_name
    @property
    def docFILE2(self):
           try:
               url = self.document.url
           except:
               url = ''
           return url

class heure(models.Model):
    heure = models.CharField(max_length=20)
    def __str__(self):
            return self.heure
class emploi(models.Model):
    heure = models.CharField(max_length=20)
    def __str__(self):
            return self.heure
class Présence(models.Model):
    professeur_qui_a_approuvé = models.ForeignKey(Professeur, on_delete=models.SET_NULL, null=True, blank=True)
    marqué_la_présence =  models.ForeignKey(Etudiant, on_delete=models.SET_NULL, null=True, blank=True)
    les_éléves_qui_vont_étre_marqué =  models.CharField(max_length=20)
    matiére = models.ForeignKey(Matiére, on_delete=models.SET_NULL, null=True, blank=True)
    présence = models.BooleanField(default=True,null=True, blank=True)
    date =  models.CharField(max_length=200)
    heure = models.ForeignKey(heure, on_delete=models.SET_NULL, null=True, blank=True)
    combien_du_heure = models.ForeignKey(emploi, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.les_éléves_qui_vont_étre_marqué

class Classe(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.SET_NULL, null=True, blank=True)
    lien = models.CharField(max_length=2000)
    matiére =  models.ForeignKey(Matiére, on_delete=models.SET_NULL, null=True, blank=True)
    date =  models.CharField(max_length=200)
    heure =  models.CharField(max_length=200)

    def __str__(self):
        return self.heure
class Live_ended (models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.SET_NULL, null=True, blank=True)
    matiére = models.ForeignKey(Matiére, on_delete=models.SET_NULL, null=True, blank=True)
    cour = models.CharField(max_length=100)
    partie = models.CharField(max_length=100)
    live = models.FileField()


    def __str__(self):
        return self.cour
    @property
    def docFILE3(self):
           try:
               url = self.live.url
           except:
               url = ''
           return url
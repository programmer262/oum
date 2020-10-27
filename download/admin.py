from django.contrib import admin
from .models import *

admin.site.site_header = "2BACSPC-F-A"
admin.site.site_title = "2BACSPC-F-A"
admin.site.register(Cour)
admin.site.register(Exercice)
admin.site.register(Corrigé)
admin.site.register(Présence)
admin.site.register(Classe)
admin.site.register(Professeur)
admin.site.register(Matiére)
admin.site.register(Live_ended)
admin.site.register(Etudiant)
admin.site.register(heure)
admin.site.register(emploi)
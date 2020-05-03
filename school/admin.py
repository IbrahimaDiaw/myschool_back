from django.contrib import admin
from .models import Etablissement
from .models import Batiment
from .models import Salle, Matiere
from .models import Classe,Niveau,AnneeScolaire, Retard, Absence

# Register your models here.
admin.site.register(Etablissement)
admin.site.register(Batiment)
admin.site.register(Salle)
admin.site.register(Matiere)
admin.site.register(Classe)
admin.site.register(AnneeScolaire)
admin.site.register(Niveau)
admin.site.register(Retard)
admin.site.register(Absence)

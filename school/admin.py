from django.contrib import admin
from .models import Etablissement
from .models import Batiment
from .models import Salle, Matiere

# Register your models here.
admin.site.register(Etablissement)
admin.site.register(Batiment)
admin.site.register(Salle)
admin.site.register(Matiere)

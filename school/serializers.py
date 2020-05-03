from rest_framework import serializers
from school.models import Etablissement
from school.models import Batiment
from school.models import Salle
from .models import AnneeScolaire, Classe, Niveau, Retard,Absence

class EtablissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etablissement
        fields = ('id',
                  'logo',
                  'nom',
                  'adresse',
                  'tel',
                  'fax')

class BatimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batiment
        fields = ('id',
                  'etablissment',
                  'nom')

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = ('id',
                  'batiment',
                  'nom',
                  'capacite')

#Serialisation de la classe AnneeScocailre
class AnneeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = AnneeScolaire
        fields = '__all__'

#Serialisation de la classe Classe
class ClasseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Classe
            fields = '__all__'

#Serialisation de la classe Niveau
class NiveauSerializer(serializers.ModelSerializer):
        class Meta:
            model = Niveau
            fields = '__all__'

#Serialiastion de la classe Retard
class RetardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retard
        fields = '__all__'

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'
from rest_framework import serializers
from school.models import Etablissement
from school.models import Batiment
from school.models import Salle

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

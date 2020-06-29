from rest_framework import serializers
from school.models import Etablissement
from school.models import Batiment
from school.models import Salle
from school.models import Professeur
from .models import AnneeScolaire, Classe, Niveau, Retard,Absence, Compte,Eleve,Parent
from django.contrib.auth.models import Permission, User, Group
from django.contrib.contenttypes.models import ContentType


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


#Serialisation de la classe Parent
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Parent
        fields = '__all__'

#Serialisation de la classe Professeur
class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model: Professeur
        fields = '__all__'

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

#Serialisation de la classe Eleve
class EleveSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Eleve
            # fields = ('id', 'photo', 'prenom',
            #       'nom', 'sexe', 'dateNaissance', 'lieuNaissance', 'adresse',
            #       'tel', 'nationnalite', 'etatSante', 'parcours', 'classe', 'parent', 'createdAt')
            fields: '__all__'

#Serialisation de la classe Compte
class CompteSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Compte
            fields = ['url', 'id', 'user', 'detenteur','profil', 'createdAt']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    compte = serializers.HyperlinkedRelatedField( view_name='compte-detail', read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'compte','password')
        extra_kwargs = {'password': {'write_only': True}}

class PermissionSerializer(serializers.HyperlinkedModelSerializer):

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)

    class Meta: 
        model = Permission
        fields = ('url', 'id', 'content_type', 'codename','name')
        # extra_kwargs = {'password': {'write_only': True}}

class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)

    class Meta: 
        model = ContentType
        fields = ('url', 'id', 'app_label', 'model')
        # extra_kwargs = {'password': {'write_only': True}}

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)

    class Meta: 
        model = Group
        fields = ('url', 'id', 'name')
        # extra_kwargs = {'password': {'write_only': True}}
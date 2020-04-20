from django.shortcuts import render
from rest_framework import generics, permissions
# from .models import Etablissement, Batiment, Salle
from .models import *
from .serializers import EtablissementSerializer, BatimentSerializer, SalleSerializer
from django.http import HttpResponse
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class EtablissementViewList(generics.ListCreateAPIView):
    queryset = Etablissement.objects.all()
    serializer_class = EtablissementSerializer

class EtablissementViewEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Etablissement.objects.all()
    serializer_class = EtablissementSerializer

class BatimentViewList(generics.ListCreateAPIView):
    queryset = Batiment.objects.all()
    serializer_class = BatimentSerializer

class BatimentViewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Batiment.objects.all()
    serializer_class = BatimentSerializer

class SalleViewList(generics.ListCreateAPIView):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer

class SalleViewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer

def RemplireBAse(request):
    """ c'est une fonction que j'ai créé juste pour remplir la base de
     données et après je vais le supprimer j'y assosité une route(remplir) """

    return HttpResponse("tout s'est bien passé")

from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
# from .models import Etablissement, Batiment, Salle
from .models import *
from .serializers import (EtablissementSerializer, BatimentSerializer, SalleSerializer, GroupSerializer,
             ClasseSerializer,NiveauSerializer,AnneeSerializer, RetardSerializer,AbsenceSerializer, 
             CompteSerializer, UserSerializer, PermissionSerializer,ContentTypeSerializer, EleveSerializer,
             ParentSerializer, ProfesseurSerializer)
from django.http import HttpResponse
# from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Permission, User, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from .permissions import *

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

class ParentViewList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentViewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_Parent = [IsAuthenticated]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ProfesseurViewList(generics.ListCreateAPIView):
    queryset = Professeur.objects.all()
    serializer_class = ParentSerializer

class ProfesseurViewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_Professeur = [IsAuthenticated]
    queryset = Professeur.objects.all()
    serializer_class = ParentSerializer


class ClasseViewList(generics.ListCreateAPIView):
    queryset  = Classe.objects.all()
    serializer_class = ClasseSerializer
    permission_classes = [IsAuthenticated]

class ClasseViewElement(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Classe.objects.all()
    serializer_class = ClasseSerializer
    permission_classes = [IsAuthenticated]

class AnneeViewList(generics.ListCreateAPIView):
    queryset  = AnneeScolaire.objects.all()
    serializer_class = AnneeSerializer
    permission_classes = [IsAuthenticated]

class AnneeViewElement(generics.RetrieveUpdateDestroyAPIView):
    queryset  = AnneeScolaire.objects.all()
    serializer_class = AnneeSerializer
    permission_classes = [IsAuthenticated]

class NiveauViewList(generics.ListCreateAPIView):
    queryset  = Niveau.objects.all()
    serializer_class = NiveauSerializer
    permission_classes = [IsAuthenticated]

class NiveauViewElement(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Niveau.objects.all()
    serializer_class = NiveauSerializer
    permission_classes = [IsAuthenticated]

class RetardViewList(generics.ListCreateAPIView):
    queryset = Retard.objects.all()
    serializer_class = RetardSerializer
    permission_classes = [IsAuthenticated]

class RetardViewElement(generics.RetrieveUpdateDestroyAPIView):
    queryset = Retard.objects.all()
    serializer_class = RetardSerializer
    permission_classes = [IsAuthenticated]


class AbsenceViewList(generics.ListCreateAPIView):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    permission_classes = [IsAuthenticated]

class AbsenceViewElement(generics.RetrieveUpdateDestroyAPIView):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    permission_classes = [IsAuthenticated]

class EleveViewList(generics.ListCreateAPIView):
    queryset  = Eleve.objects.all()
    serializer_class = EleveSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['prenom', 'nom']
class ElevesViewElement(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer
    permission_classes = [IsAuthenticated]


def RemplireBAse(request):
    """ c'est une fonction que j'ai créé juste pour remplir la base de
     données et après je vais le supprimer j'y assosité une route(remplir) """

    return HttpResponse("tout s'est bien passé")


class CompteViewList(viewsets.ModelViewSet):
    queryset  = Compte.objects.all()
    serializer_class = CompteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        print(self.request.user.is_authenticated)
        print(self.request.auth)
        serializer.save()


    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def user_permissions(self, request, format=None):
        """ Return user permissions. """
        user = None
        pk = request.query_params.get('user_id')
        if pk is not None:
            user = get_object_or_404(User, pk = pk)
        else :
            user = request.user
        permissions = user.get_all_permissions()
        return Response({'%s_permissions'%(user.username) : permissions})

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def user_groups(self, request, format=None):
        """ Return user permissions. """
        user = None
        pk = request.query_params.get('user_id')
        if pk is not None:
            user = get_object_or_404(User, pk = pk)
        else :
            user = request.user
        groups = [{'id' :group.id,'name' : group.name} for group in user.groups.all()]
        return Response({'%s_groups'%(user.username) : groups})
class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAdminUser|IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


    

    # @action(detail=True, methods=['get'], permission_classes=[IsAdminOrIsSelf])
    # def user_permissions(self, request, format=None):
    #     """ Return user permissions. """
    #     user = None
    #     group = None
    #     user_id = request.GET.get('user_id')
    #     group_id = request.GET.get('group_id')
    #     content_types = ContentType.objects.all()
    #     permissions = {}
    #     if user_id is not None:
    #         user = get_object_or_404(User, pk = user_id)
    #     elif group_id is not None:
    #         group = get_object_or_404(Group, pk = group_id)
    #     else :
    #         user = request.user

    #     print(user)
    #     print(group)

    #     if user is not None :
    #         for content_type in content_types:
    #             perm={}
    #             perm['add'] = user.has_perm(content_type.app_label + '.add_' + content_type.model)
    #             perm['change'] = user.has_perm(content_type.app_label + '.change_' + content_type.model)
    #             perm['delete'] = user.has_perm(content_type.app_label + '.delete_' + content_type.model)
    #             perm['view'] = user.has_perm(content_type.app_label + '.view_' + content_type.model)
    #             permissions[content_type.model] = perm
    #     elif group is not None :
    #         print('je suis là')
    #         for permission in group.permissions:
    #             perm={}
    #             perm['add'] = group.has_perm(content_type.app_label + '.add_' + content_type.model)
    #             perm['change'] = group.has_perm(content_type.app_label + '.change_' + content_type.model)
    #             perm['delete'] = group.has_perm(content_type.app_label + '.delete_' + content_type.model)
    #             perm['view'] = group.has_perm(content_type.app_label + '.view_' + content_type.model)
    #             permissions[content_type.model] = perm

    #     return Response(permissions)

class ContentTypeViewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
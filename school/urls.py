from django.urls import path
from .views import *


urlpatterns= [
    path('etablissement/', EtablissementViewList.as_view()),
    path('etablissement/<int:pk>/', EtablissementViewEdit.as_view()),

    path('batiment/', BatimentViewList.as_view()),
    path('batiment/<int:pk>/', BatimentViewDetail.as_view()),

    path('salle/',  SalleViewList.as_view()),
    path('salle/<int:pk>/', SalleViewDetail.as_view()),

    path('classe/', ClasseViewList.as_view()),
    path('classe/<int:pk>', ClasseViewElement.as_view()),
    
    path('niveau/', NiveauViewList.as_view()),
    path('niveau/<int:pk>', NiveauViewElement.as_view()),
    
    path('anneescolaire/', AnneeViewList.as_view()),
    path('anneescolaire/<int:pk>', AnneeViewElement.as_view()),

    path('remplir/', RemplireBAse),


]

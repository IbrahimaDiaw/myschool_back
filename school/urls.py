from django.urls import path
from .views import *
from .router import router
from django.conf.urls import include, url

urlpatterns= [
    path('', include(router.urls)),

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

    path('retard/', RetardViewList.as_view()),
    path('retard/<int<:pk', RetardViewElement.as_view()),

    path('absence', AbsenceViewList.as_view()),
    path('absence/<int:pk>', AbsenceViewElement.as_view()),

    path('eleves/', EleveViewList.as_view()),
    path('eleves/<int>:pk', ElevesViewElement.as_view()),
    
    path('parents/', ParentViewList.as_view()),
    path('parents/<int>:pk', ParentViewDetail.as_view()),
    
    path('professeur/', ProfesseurViewList.as_view()),
    path('professeur/<int>:pk', ProfesseurViewDetail.as_view()),

    path('remplir/', RemplireBAse),

    path('api-auth/', include('rest_framework.urls')),
]

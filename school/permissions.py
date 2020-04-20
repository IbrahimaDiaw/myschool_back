from rest_framework import permissions

"""cette classe est créé pour gerer les lecture et modification et suppression
    C'est-à-dire seule l'utilisateur qui a ajouter le l'etablissement
    peut y  apporter les modeifications"""

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Les autorisations en lecture seule sont autorisées pour toute demande
        if request.method in permissions.SAFE_METHODS:
            return True

        # Les autorisations d'écriture ne sont accordées qu'à l'auteur
        return obj.author == request.user

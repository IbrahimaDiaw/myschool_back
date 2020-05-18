from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Etablissement(models.Model):
    """docstring for Etablissement."""
    logo = models.ImageField(upload_to='Images')
    nom = models.CharField(max_length = 50)
    adresse = models.CharField(max_length = 140)
    tel = models.IntegerField()
    active = models.BooleanField(default = True)
    fax = models.IntegerField()
    createdAt = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nom

class Batiment(models.Model):
    """docstring for Batiment."""
    etablissment = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    active = models.BooleanField(default = True)
    nom = models.CharField(max_length = 100)
    createdAt = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nom

class Salle(models.Model):
    """docstring for Salle."""
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    nom = models.CharField(max_length = 100)
    active = models.BooleanField(default = True)
    capacite = models.IntegerField()
    createdAt = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nom

class Parent(models.Model):
    """docstring for Parent."""
    prenom = models.CharField(max_length = 80)
    nom = models.CharField(max_length = 80)
    adresse = models.CharField(max_length = 255)
    cin = models.IntegerField()
    tel = models.IntegerField()
    createdAt = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.prenom +' '+ self.nom

class Professeur(models.Model):
    """docstring for Professeur."""
    etablissment = models.ForeignKey(Etablissement, on_delete = models.CASCADE)
    prenom = models.CharField(max_length = 100)
    nom = models.CharField(max_length = 100)
    adresse = models.CharField(max_length = 250)
    civilite = models.CharField(max_length = 5)
    dateNaissance = models.DateField()
    lieuNaissance = models.CharField(max_length = 100)
    tel = models.IntegerField()
    email = models.EmailField()
    niveau_etude = models.CharField(max_length = 100)
    specialite = models.CharField(max_length = 100)
    createdAt = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.prenom +' '+ self.nom

class AnneeScolaire(models.Model):
    """la classe année scolaire """
    anneeDebut = models.IntegerField()
    anneeFin = models.IntegerField()

class Niveau(models.Model):
    """ le model qui definit le niveau """
    niveau = models.CharField(max_length = 45)

    def __str__(self):
        return self.niveau

class Classe(models.Model):
    """le model des classe de l'etablissment """
    nomClasse = models.CharField(max_length = 100)
    AnneeScolaire = models.ForeignKey(AnneeScolaire, on_delete = models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete = models.CASCADE)

    createdAt = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nomClasse

class Eleve(models.Model):
    """model qui définit les élèves"""
    photo = models.ImageField(upload_to='Images')
    prenom = models.CharField(max_length = 100)
    nom = models.CharField(max_length=100)
    sexe = models.CharField(max_length = 30)
    dateNaissance = models.DateField()
    lieuNaissance = models.CharField(max_length = 100)
    adresse = models.CharField(max_length = 255)
    tel  = models.IntegerField()
    nationnalite = models.CharField(max_length = 100)
    etatSante = models.CharField(max_length = 80)
    parcours = models.TextField()
    classe = models.ForeignKey(Classe,blank=True, null=True, on_delete = models.SET_NULL)
    parent = models.ForeignKey(Parent,blank=True, null=True, on_delete = models.SET_NULL)
    createdAt = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.prenom +' '+ self.nom

class  Matiere(models.Model):
    """le model des matières enseignées au sein l'établissement"""
    intitule = models.CharField(max_length = 85)
    professeur = models.ForeignKey(Professeur, on_delete = models.CASCADE)
    suivre = models.ManyToManyField(Niveau, through = 'Matiere_has_Niveau')
    createdAt = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.intitule

class Matiere_has_Niveau(models.Model):
    coef = models.IntegerField()
    niveau = models.ForeignKey(Niveau, on_delete = models.CASCADE, related_name ="niveau_mats")
    matiere = models.ForeignKey(Matiere, on_delete = models.CASCADE, related_name ="mat_niveaux")


class Evaluation(models.Model):
    """le model qui définit les évaluations des élèves"""
    libelle = models.CharField(max_length = 80)
    date = models.DateField()
    duree = models.CharField(max_length = 20)
    matiere = models.ForeignKey(Matiere, on_delete = models.CASCADE)
    participants = models.ManyToManyField(Eleve, through = 'Eleve_has_Evaluation')
    createdAt = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.libelle

class Eleve_has_Evaluation(models.Model):
    """la classe qui reportorie les notes obtenues par les eleves aucours des evaluations"""
    eleve = models.ForeignKey(Eleve, on_delete = models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete = models.CASCADE, related_name= "eval_eleve",)
    note = models.FloatField()

class Emploi_temps(models.Model):
    """le model qui gére les Emploi_temps """
    heureDebut = models.TimeField()
    heureFin = models.TimeField()
    jours = models.DateField()
    matiere = models.ForeignKey(Matiere, on_delete = models.CASCADE)
    prof = models.ForeignKey(Professeur, on_delete = models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete = models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete = models.CASCADE)


class Retard(models.Model):
    """gestion des Retard prof & eleve """
    date = models.DateField()
    motif = models.TextField()
    eleve = models.ForeignKey(Eleve, on_delete = models.CASCADE, null = True)
    emploitemps = models.ForeignKey(Emploi_temps, on_delete = models.CASCADE)
    prof = models.ForeignKey(Professeur, on_delete = models.CASCADE, null = True)


class Absence(models.Model):
    """gestion des absences prof & eleve """
    date = models.DateField()
    motif = models.TextField()
    eleve = models.ForeignKey(Eleve, on_delete = models.CASCADE, null = True)
    emploitemps = models.ForeignKey(Emploi_temps, on_delete = models.CASCADE)
    prof = models.ForeignKey(Professeur, on_delete = models.CASCADE, null = True)


class Compte(models.Model):
    user =models.OneToOneField(User, on_delete = models.CASCADE, related_name= "compte")
    detenteur = models.IntegerField(null=True)
    profil = models.CharField(max_length = 80, null = True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['detenteur', 'profil']]
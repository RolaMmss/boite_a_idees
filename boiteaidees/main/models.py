from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Idee(models.Model):
    formulation = models.CharField(max_length=100)
    detail = models.CharField(max_length=200, null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    # nb_vote_positif = 

class Votant(models.Model):
    votant = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Idee, on_delete=models.CASCADE)
    type_vote = models.BooleanField()
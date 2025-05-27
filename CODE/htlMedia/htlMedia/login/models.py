from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    roles = models.CharField(max_length=3,choices=(
        (0,"admin"),(1,"schueler"),
    ))

    def __str__(self):
      return self.username
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    Class = models.CharField(max_length=3,choices=(
        ("1a","1A"),("1b","1B"),
        ("2a","2A"),("2b","2B"),
        ("3a","3A"),("3b","3B"),
        ("4a","4A"),("4b","4B"),
        ("5a","5A"),("5b","5B"),
    ))
    deparment = models.CharField(max_length=5,choices=(
        ("IT","HIT"),
        ("WIM","HWIM"),
        ("MBA","HMBA"),
        ("ET","HET"),
        ("AFME","AFME")
    ))

    def __str__(self):
      return self.username
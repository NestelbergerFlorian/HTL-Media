from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    titel = models.CharField(max_length=255,default="Titel")
    image_file = models.ImageField(upload_to='images/')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    main_Tag = models.CharField(max_length=20,choices=(
        ("1","3AHIT"),
   ))
from django.db import models
from login.models import User

# Create your models here.
class Post(models.Model):
    titel = models.CharField(max_length=30)
    image_file = models.ImageField(upload_to='images/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    main_Tag = models.CharField(max_length=20,choices=(
        ("1","3AHIT"),
   ))
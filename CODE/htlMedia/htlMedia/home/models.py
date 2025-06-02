from django.db import models
from login.models import User

# Create your models here.
class Post(models.Model):
    titel = models.CharField(max_length=30)
    image_file = models.ImageField(upload_to='images/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField()
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    Description = models.CharField(max_length=300)
    main_Tag = models.CharField(max_length=20,choices=(
        ("1","1AHIT"),("2","2AHIT"),("3","3AHIT"),("4","4AHIT"),("5","5AHIT"),
    ))

    @property
    def total_likes(self):
        return self.likes.count()

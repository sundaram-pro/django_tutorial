from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_lenght=75)
    body=models.TextField()
    slug=models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
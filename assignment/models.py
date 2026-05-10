from django.db import models

# Create your models here.
class About(models.Model):
    about_title=models.CharField(max_length=60)
    about_description=models.TextField(max_length=233)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Social(models.Model):
    name=models.CharField(max_length=50)
    link=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
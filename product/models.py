from django.db import models

# Create your models here.


class Item(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='uploads')
    date=models.DateTimeField(auto_now_add=True)
    

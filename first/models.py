from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Ntodo(models.Model):
    title=models.CharField(max_length=30)
    desc=models.TextField(max_length=300)
    important=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    

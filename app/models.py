from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F
from django.utils import timezone

class UserInput(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='payload' ,blank=True,null=True)
    number = models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
       return str(self.number)
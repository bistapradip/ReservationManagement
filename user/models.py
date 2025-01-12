from django.db import models
from django.contrib.auth.models import User

#Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='ProfileImage/')

    
    def __str__(self):
        return f'{self.staff.username}--Profile'
    

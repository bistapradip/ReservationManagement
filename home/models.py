from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User

# Create your models here.

Sector = (
    ('KTM/MTN', 'KTM-MTN'),
    ('KTM/PKR', 'KTM-PKR'),
    ('PKR/KTM', 'PKR-KTM'),
    ('KTM/BWA', 'KTM-BWA'),
    ('BWA/KTM', 'BWA-KTM'),
    ('KTM/BIR', 'KTM-BIR'),
    ('BIR/KTM', 'BIR-KTM'),
    ('KTM/KEP', 'KTM-KEP'),
    ('KEP/KTM', 'KEP-KTM'),
    ('KTM/BHR', 'KTM-BHR'),
    ('BHR/KTM', 'BHR-KTM'),
    ('KTM/SKH', 'KTM-SKH'),
    ('SKH/KTM', 'SKH-KTM'),
    ('KTM/DHI', 'KTM-DHI'),
    ('DHI/KTM', 'DHI-KTM'),
    ('PKR/BWA', 'PKR-BWA'),
    ('BWA/PKR', 'BWA-PKR'),
    ('PKR/BIR', 'PKR-BIR'),
    ('BIR/PKR', 'BIR-PKR'),
    ('PKR/KEP', 'PKR-KEP'),
    ('KEP/PKR', 'KEP-PKR'),
    ('PKR/BHR', 'PKR-BHR'),
    ('BHR/PKR', 'BHR-PKR'),
    ('KTM/LUA', 'KTM-LUA'),  
    ('LUA/KTM', 'LUA-KTM'),  
    ('KTM/PPL', 'KTM-PPL'),  
    ('PPL/KTM', 'PPL-KTM'),  
    ('KTM/TMI', 'KTM-TMI'), 
    ('TMI/KTM', 'TMI-KTM'),  
    ('KTM/RHP', 'KTM-RHP'),  
    ('RHP/KTM', 'RHP-KTM'),  
    ('LUA/PPL', 'LUA-PPL'), 
    ('PPL/LUA', 'PPL-LUA'),  
    ('LUA/TMI', 'LUA-TMI'),  
    ('TMI/LUA', 'TMI-LUA'),  
    ('PPL/TMI', 'PPL-TMI'),  
    ('TMI/PPL', 'TMI-PPL'),  
    ('LUA/RHP', 'LUA-RHP'),  
    ('RHP/LUA', 'RHP-LUA'),  
    ('PPL/RHP', 'PPL-RHP'),  
    ('RHP/PPL', 'RHP-PPL'), 
    ('PKR/JOM', 'PKR-JOM'),
    ('JOM/PKR', 'JOM-PKR'),
    ('KEP/IMK', 'KEP-IMK'),
    ('IMK/KEP', 'IMK-KEP'),
    ('KEP/DOP', 'KEP-DOP'),
    ('DOP/KEP', 'DOP-KEP'),
    
)
class staff(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.BigIntegerField()
    image = models.ImageField(upload_to='staffImage/')

    
    def image_tag(self):
        return format_html("<img src = '/media/{}' style= width:50px;height:50px/>".format(self.image))

class Confirmed(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    sector = models.CharField(max_length=50, choices=Sector)
    paxNo = models.CharField(max_length=8)
    agency = models.CharField(max_length=50)
    airline = models.CharField(max_length=15)
    flightno = models.IntegerField()
    remarks = models.CharField(max_length=50)
    reference = models.CharField(max_length=30)
    staff = models.ForeignKey(User, models.CASCADE, null = True)

    def __str__(self):
        return f'{self.sector}--{self.agency}'

class Enquiry(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=50, null=True)
    ttl = models.DateTimeField(default=None)
    sector = models.CharField(max_length=10)
    paxNo = models.CharField(max_length=8)
    agency = models.CharField(max_length=50)
    airline = models.CharField(max_length=15)
    flighttime = models.TimeField(default=None)
    remarks = models.CharField(max_length=50)
    reference = models.CharField(max_length=50)
    staff = models.ForeignKey(User, models.CASCADE,null=True)

    def __str__(self):
        return f'{self.sector}--{self.agency}'

class FOC(models.Model):
    date = models.DateField(auto_now = False, auto_now_add = False)
    sector = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    flightno = models.IntegerField()
    paxno = models.IntegerField()
    reference = models.CharField(max_length=20)


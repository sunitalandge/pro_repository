from django.db import models
from multiselectfield import MultiSelectField
import datetime

class Client_info(models.Model):
    client_uname= models.CharField(primary_key=True,max_length=100)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email = models.EmailField(max_length= 90)
    mobile = models.IntegerField()
    location = models.CharField(max_length= 50)
    expr = models.IntegerField()
    def __str__(self):
        return self.client_uname

class Client_pro(models.Model):
    client_uname = models.ForeignKey(Client_info)
    pro_name=models.CharField(max_length= 100)
    pro_desc = models.CharField(max_length= 500)
    #pro_link = models.FileField(upload_to='files')
    pro_days = models.IntegerField()
    comp_name = models.CharField(max_length=100)
    def __str__(self):
        return  self.pro_name

class Client_expr_info(models.Model):
    client_uname = models.ForeignKey(Client_pro)
    comp_name = models.CharField(max_length= 400)
    start_day = models.DateField(auto_now=True)
    end_day = models.DateField()
    def __str__(self):
        return self.comp_name

class Pro_lang(models.Model):
    client_uname = models.ForeignKey(Client_expr_info)
    LANG_CHOICES = (
        ('Python', 'Python'),
        ('django', 'Django'),
        ('api', 'API'),
        ('ui', 'UI'),
        ('flask', 'Flask')
    )
    languages = MultiSelectField(max_length=200, choices=LANG_CHOICES)
    percentage = models.IntegerField()

    def __str__(self):
        return self.client_uname

class Client_certification(models.Model):
    client_uname = models.ForeignKey(Pro_lang)
    certificate_name = models.CharField(max_length=400)
    year = models.DateTimeField()

    def __str__(self):
        return self.client_uname
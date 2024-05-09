from django.db import models

# Create your models here.
class details(models.Model):

    name = models.CharField(max_length=100)
    disccc = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='hari',null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    des = models.TextField()
    # id : int
    # name : str
    # img : str
    # desc : str
    # price : int



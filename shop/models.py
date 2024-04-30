from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Catagory(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class shopname(models.Model):
     catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
     shop_name=models.CharField(max_length=150,null=False,blank=False)
     shop_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
     
     def __str__(self):
        return self.shop_name
     
     
class Product(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    shop_name=models.ForeignKey(shopname,on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    product_image1=models.ImageField(upload_to=getFileName,null=True,blank=True)
    product_image2=models.ImageField(upload_to=getFileName,null=True,blank=True)
    product_image3=models.ImageField(upload_to=getFileName,null=True,blank=True)
    product_image4=models.ImageField(upload_to=getFileName,null=True,blank=True)
    product_image5=models.ImageField(upload_to=getFileName,null=True,blank=True)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    address=models.CharField(max_length=250,null=False,blank=False)
    phone_no=models.CharField(max_length=50,null=False,blank=True)
    e_mail=models.CharField(max_length=150,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")

    def __str__(self):
        return self.name
    



    
    
    


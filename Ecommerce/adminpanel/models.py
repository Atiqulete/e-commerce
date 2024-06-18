from django.db import models
from django.contrib.auth.models import AbstractUser


class usertype(models.Model):
    type_name = models.CharField(max_length=200)

class User(AbstractUser):
    user_type = models.ForeignKey(usertype,on_delete=models.CASCADE,default = 1)

class category(models.Model):
    category_name = models.CharField(max_length=200)
    category_img = models.ImageField(upload_to='category/',blank=True,null=True)

class product(models.Model):
    product_name =models.CharField(max_length=200)
    product_old_price =models.FloatField()
    product_new_price =models.FloatField()
    product_category =models.ForeignKey(category,on_delete=models.CASCADE,related_name='cat')

class product_img(models.Model):
    product_Image_all = models.ImageField(upload_to='product/',blank=True,null=True)
    product_table = models.ForeignKey(product,on_delete=models.CASCADE,related_name='prod')

class slider(models.Model):
    discount = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider/', blank= True,null=True)
    is_delete = models.BooleanField(default=False)


from django.db import models
from adminpanel.models import product,product_img
class customer(models.Model):
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(max_length=200)
    mobile = models.IntegerField()
    password = models.CharField(max_length=200)

    @staticmethod
    def customer_check(c):
        try:
            return customer.objects.get(username = c)
        except:
            return False
        
class wishlist(models.Model):
    product_id = models.ForeignKey(product,on_delete=models.SET_NULL,blank=True,null=True)
    customer_id = models.ForeignKey(customer,on_delete=models.SET_NULL,blank=True,null=True)
    wish_date = models.DateField(auto_now=True)
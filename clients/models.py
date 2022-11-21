from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Outlets(models.Model):
    outlet_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    outlet_name=models.CharField(max_length=100)
    owner_name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    logo=models.TextField()
    description=models.TextField()
    
    def __str__(self):
        return self.outlet_name

class Products(models.Model):
    outlet_id=models.ForeignKey(Outlets,null=False,on_delete=models.DO_NOTHING)
    product_id=models.UUIDField(primary_key=True,null=False, default=uuid.uuid4, editable=False)
    product_name=models.CharField(max_length=100)
    stock_quatity=models.IntegerField(default=0)
    price=models.FloatField(default=0.0)
    description=models.TextField()
    def __str__(self):
        return self.product_name
    
class Orders(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    outlet_id=models.ForeignKey(Outlets, on_delete=models.DO_NOTHING)
    order_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list=ArrayField(base_field=models.CharField(max_length=100))
    timestamp=models.DateTimeField(auto_now_add=True)
    address=models.TextField()
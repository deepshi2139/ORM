from django.db import models
from django.contrib import admin
class customer(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    customer_name=models.CharField(max_length=10)
    Date=models.DateField()
    Email=models.EmailField()
    Address=models.TextField()
    Phonenumber=models.IntegerField()
    price=models.IntegerField()
    productname=models.CharField(max_length=10)

class customerAdmin(admin.ModelAdmin):
    list_display=["customer_id","customer_name","Date","Email","Address","Phonenumber","price","productname"]

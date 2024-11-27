from django.db import models

# Create your models here.

class contact(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class signup_db(models.Model):
    Username1 = models.CharField(max_length=100, null=True, blank=True)
    Contact = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password1 = models.CharField(max_length=100, null=True, blank=True)
    Password2 = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    Quantity = models.CharField(max_length=100, null=True, blank=True)
    Product = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Tprice = models.IntegerField(null=True, blank=True)
    Uname = models.CharField(max_length=100, null=True, blank=True)
    Pro_Image = models.ImageField(upload_to='Cart_images', null=True, blank=True)

class orderdb(models.Model):
    Fname = models.CharField(max_length=100, null=True, blank=True)
    Lname = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100,null=True, blank=True)
    Address = models.TextField(max_length=100,null=True, blank=True)
    Zip = models.IntegerField(null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Town = models.CharField(max_length=100, null=True, blank=True)
    Comment = models.CharField(max_length=100, null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)



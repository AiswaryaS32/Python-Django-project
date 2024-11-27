from django.db import models

# Create your models here.

class category(models.Model):
    ccname = models.CharField(max_length=100, null=True, blank=True)
    cimage = models.ImageField(upload_to="category_images",null=True, blank=True)
    cdesc = models.CharField(max_length=100, null=True, blank=True)


class product(models.Model):
    pname = models.CharField(max_length=100, null=True, blank=True)
    pcat = models.CharField(max_length=100, null=True, blank=True)
    pquan = models.IntegerField(null=True, blank=True)
    pprice = models.IntegerField(null=True, blank=True)
    pimage1 = models.ImageField(upload_to="p_images",null=True, blank=True)
    pimage2 = models.ImageField(upload_to="p_images",null=True, blank=True)
    pimage3 = models.ImageField(upload_to="p_images",null=True, blank=True)
    pman = models.CharField(max_length=100, null=True, blank=True)
    coun = models.CharField(max_length=100, null=True, blank=True)
    pdesc = models.CharField(max_length=100, null=True, blank=True)
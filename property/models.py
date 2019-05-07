from django.db import models
from cms.models import CMSPlugin

# Create your models here.
# class for type of property: house, office,...
class PropertyType(models.Model):
    id = models.AutoField(primary_key=True)
    type=models.CharField(max_length=100,blank=False,null=False)
    def __str__(self):
        return self.type

# class for place/location of property: city, area...
class PropertyPlace(models.Model):
    id = models.AutoField(primary_key=True)
    place=models.CharField(max_length=100,blank=False,null=False)
    def __str__(self):
        return self.place

# class for floor in which property is located
class PropertyFloor(models.Model):
    id = models.AutoField(primary_key=True)
    floor=models.CharField(max_length=100,blank=False,null=False)
    def __str__(self):
        return self.floor

# class for seller of property
class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=False,null=False)
    phone=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    address=models.CharField(max_length=200,blank=True,null=True)
    agent=models.BooleanField(default=True)
    def __str__(self):
        return self.name

# class for property including all features
class Property(models.Model):
    id = models.AutoField(primary_key=True)
    type=models.ForeignKey(PropertyType,default='')
    place=models.ForeignKey(PropertyPlace,default='')
    seller=models.ForeignKey(Seller,default='')
    #floor=models.ForeignKey(PropertyFloor,default='')
    floor=models.IntegerField(default=0)

    name=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=200,blank=True,null=True)

    forSale=models.BooleanField(default=True)
    fitted=models.BooleanField(default=True)
    furnished=models.BooleanField(default=True)
    featured=models.BooleanField(default=True)
    display=models.BooleanField(default=True)

    area=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)
    dateAvailable=models.DateTimeField(blank=True,null=True)
    description=models.TextField(default='')
    img1=models.ImageField(upload_to="img/", null=True, blank=True)
    img2=models.ImageField(upload_to="img/", null=True, blank=True)
    img3=models.ImageField(upload_to="img/", null=True, blank=True)
    img4=models.ImageField(upload_to="img/", null=True, blank=True)
    img5=models.ImageField(upload_to="img/", null=True, blank=True)
    showPrice=models.BooleanField(default=True)
    showSellerPhone=models.BooleanField(default=False)
#    def __init__(self):
#        super(Property, self).__init__()
    def __str__(self):
        return self.name

# class to deal with all contacts of users with the website, such as questions, property requests, property offers..
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    type=models.CharField(max_length=100,blank=False,null=False,default='contact')
    name=models.CharField(max_length=100,blank=False,null=False)
    phone=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    subject=models.CharField(max_length=200,blank=True,null=True)
    message=models.TextField()
    checked=models.BooleanField(default=False)
    display=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name



class PropertyPlugin(CMSPlugin):
    property = models.ForeignKey('Property', related_name='plugins')

    def __unicode__(self):
      return self.property.name
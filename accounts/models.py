from django.db import models


# Create your models here.
class Phone(models.Model):
    TYPE = (
        ('Home' , 'Home'),
        ('Mobile' , 'Mobile'),
        ('Office' , 'Office')
    )
    Number = models.IntegerField( null=True )
    Number_type = models.CharField(max_length=200 , null=True , choices=TYPE )
    def __getval__(self):
        return self.Number
    
class Email(models.Model):
    TYPE = (
        ('Home' , 'Home'),
        ('Personal' , 'Personal'),
        ('Office' , 'Office'),
        ('College' , 'College')
    )
    email = models.CharField(max_length=200 , null=True)
    email_type = models.CharField(max_length=200 , null=True , choices=TYPE )
    phone = models.ForeignKey(Phone, null=True , on_delete= models.SET_NULL)
  
    def __str__(self):
        return self.email


class SocialMedia(models.Model):
    APP = (
        ('Facebook' , 'Facebook'),
        ('Instagram' , 'Instagram'),
        ('Twitter' , 'Twitter'),
        ('Linkdin' , 'Linkdlin')
    )
    User_Name = models.CharField(max_length=200 , null=True)
    Linked_App = models.CharField(max_length=200 , null=True , choices=APP )

    def __str__(self):
        return self.User_Name
    


class Person(models.Model):
    #id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=200 , null=True)
    last_name = models.CharField(max_length=200 , null=True)
    phone = models.ForeignKey(Phone, null=True , on_delete= models.SET_NULL)
    email = models.ForeignKey(Email, null=True , on_delete= models.SET_NULL)



    def __str__(self):
        return self.first_name


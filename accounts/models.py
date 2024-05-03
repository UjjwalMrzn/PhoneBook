from django.db import models


# Create your models here.

# class ID(models.Model):
#     Id = models.AutoField(null=True)

#     def __str__(self):
#         return str(self.Id)
    


class Phone(models.Model):
    TYPE = (
        ('Home' , 'Home'),
        ('Mobile' , 'Mobile'),
        ('Office' , 'Office'),
        ('College' , 'College'),
    )
    Number = models.IntegerField( null=True )
    Number_type = models.CharField(max_length=200 , null=True , choices=TYPE )
    def __str__(self):
        return str(self.Number)
    

class Address(models.Model):
    TYPE = (
        ('Home' , 'Home'),
        ('Office' , 'Office'),
        ('College' , 'College')
    )
    Address = models.CharField(max_length=200 , null=True)
    Address_type= models.CharField(max_length=200 , null=True , choices=TYPE )
    
    def __str__(self):
        return str(self.Address)
    
class Email(models.Model):
    TYPE = (
        ('Home' , 'Home'),
        ('Personal' , 'Personal'),
        ('Office' , 'Office'),
        ('College' , 'College')
    )
    email = models.CharField(max_length=200 , null=True)
    email_type = models.CharField(max_length=200 , null=True , choices=TYPE )
  
    def __str__(self):
        return str(self.email)


class SocialMedia(models.Model):
    APP = (
        ('Facebook' , 'Facebook'),
        ('Instagram' , 'Instagram'),
        ('Twitter' , 'Twitter'),
        ('Linkdin' , 'Linkdlin'),
        ('Snapchat' , 'Snapchat'),
        ('WeChat' , 'WeChat'),
        ('Discord' , 'Discord'),
    )
    User_Name = models.CharField(max_length=200 , null=True)
    Linked_App = models.CharField(max_length=200 , null=True , choices=APP )

    def __str__(self):
        return str(self.User_Name)
    


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200 , null=True)
    last_name = models.CharField(max_length=200 , null=True)
    phone = models.ForeignKey(Phone, null=True , on_delete= models.SET_NULL)
    address = models.ForeignKey(Address, null=True , on_delete= models.SET_NULL)
    email = models.ForeignKey(Email, null=True , on_delete= models.SET_NULL)
    media = models.ForeignKey(SocialMedia, null=True , on_delete= models.SET_NULL)



    def __str__(self):
        return str(self.first_name)

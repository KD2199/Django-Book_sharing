from django.db import models
from django.contrib.auth.models import User

class Available_Books(models.Model):
   
    BookName = models.CharField(max_length=35)
    Ownername = models.CharField(max_length=35,default="")
    Edition = models.IntegerField()
    AuthorName = models.CharField(max_length=25)
    Publication = models.CharField(max_length=25)
    BookCategory = models.CharField(max_length=25)
    img = models.ImageField(upload_to='pics')
    pdf = models.FileField(upload_to='pdf')
    Department = models.CharField(max_length=25)
    Semester=models.IntegerField()
    Return=models.CharField(max_length=25,default="")
   
    

    def __str__(self):
                
         return self.BookName
    

class Available_Stationary(models.Model):
   
    Stationary_Name = models.CharField(max_length=35)
    img = models.ImageField(upload_to='SImage')
    Stationary_Description= models.CharField(max_length=1000)
    

    def __str__(self):
                
         return self.Stationary_Name
    
class Total_books(models.Model):
   
    User=models.CharField(max_length=35)
    Number_Of_Books_Donate=models.IntegerField()
    

    def __str__(self):
                
         return self.User


class Sent_Messages(models.Model):
   
    Message=models.CharField(max_length=1000)
    

    def __str__(self):
                
         return self.Message
    
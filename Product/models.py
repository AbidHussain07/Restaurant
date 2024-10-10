from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Itemlist(models.Model):
    category_name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.category_name

class Users(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)
    
class Items(models.Model):
    item_name = models.CharField(max_length=25)
    description = models.TextField(blank=False)
    price = models.IntegerField(default=100)
    category = models.ForeignKey(Itemlist , related_name='category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Items/')
    
    def __str__(self):
        return self.item_name
    
class About(models.Model):
    description = models.TextField(blank=False)

class Feedback(models.Model):
    username = models.CharField(max_length=25)
    description = models.TextField(blank=False)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.username
    
# class BookTable(models.Model):
#     name = models.CharField(max_length=25)
#     phone_no = models.IntegerField()
#     email = models.EmailField()
#     total_member = models.IntegerField()
#     date = models.DateField()
    
#     def __str__(self):
#         return self.name
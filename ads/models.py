from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    

class ads(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    des_and_detail = models.TextField()
    price = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    amount = models.IntegerField()
    image = models.ImageField(blank=True, null=True)
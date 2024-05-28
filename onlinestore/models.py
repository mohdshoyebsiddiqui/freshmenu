from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=70)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    des=models.TextField()
    ingredient=models.TextField()
    category=models.ForeignKey(Category, max_length=60,on_delete=models.CASCADE) 
    image=models.FileField(upload_to='static/product/')   


class Order(models.Model):
    name=models.CharField(max_length=70)
    price=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_status=models.CharField(max_length=100,default='cart')
    quantity=models.IntegerField(default=1)

    # placed , confirm , cancel , 

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.IntegerField()


class Comments(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.IntegerField()
    name=models.CharField(max_length=500)


class Follow(models.Model):
    user=models.CharField(max_length=100)
    followers=models.CharField(max_length=100)



class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    userid=models.IntegerField(unique=True)
    profilepic=models.FileField(upload_to='static/image',default='static/image/profile.jpg')
    bio=models.TextField()
    address=models.CharField(max_length=100)
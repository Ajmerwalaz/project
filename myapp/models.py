from django.db import models
from .models import *
from django.db.models import Sum


# Create your models here.
class user(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    password= models.CharField(max_length=50)
    phone_number=models.IntegerField(blank=True,null=True)
    image=models.ImageField(upload_to='image', blank=True,null=True)
    otp=models.IntegerField(blank=True,null=True)
    
class category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to="image")
    category=models.ForeignKey(category,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name
    

class wishlist(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - {self.product.name}"
    

class Cart(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    added_at = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"{self.user.name} - {self.product.name} (x{self.quantity})"
    
class Billing_Details(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.user.name} - {self.first_name} {self.last_name}"
from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User



class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Product(models.Model):
    CONDITION_CHOICES = (('New', 'New'), ('Sale', 'Sale'))
    STOCK_CHOICES = (('Available', 'Available'), ('Out Of Stock', 'Out Of Stock'))
    STATUS_CHOICES = (('Publish', 'Publish'), ('Draft', 'Draft'))

    unique_id = models.CharField(unique=True, max_length=200, null=True, blank=True)

    image = models.ImageField(upload_to='Product_images/img')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=100, default="New")
    information = models.TextField(default="No information provided")  # Set default value
    description = models.TextField(default="No description provided")  # Set default value
    stock = models.CharField(choices=STOCK_CHOICES, max_length=200, default='Available')  # Set default value
    status = models.CharField(choices=STATUS_CHOICES, max_length=200, default='Draft')  # Set default value
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)  # Replace 1 with the actual default ID

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.created_date.strftime('%Y%m%d%H%M%S') + str(self.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    



class order(models.Model):
    
    shipping_method = (('Standard Delivery', 'Standard Delivery'), ('Express Delivery', 'Express Delivery'))

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname =  models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email =     models.EmailField(max_length=100)
    address1 =  models.TextField()
    address2 =  models.TextField()
    country =   models.CharField(max_length=100)
    state =     models.CharField(max_length=100)
    pincode =   models.IntegerField(null=True)
    payment_id = models.CharField(max_length=300,null=True,blank=True)
    paid =      models.BooleanField(default=False,null=True)
    created_at = models.DateTimeField( default=timezone.now)
    amount =    models.CharField(max_length=100)
    delivery =  models.CharField(choices=shipping_method, max_length=200, default='Standard Delivery')

def __str__(self):
    return f"Order {self.id} by {self.user.username}"



    


class orderitem(models.Model):
    order = models.ForeignKey(order,on_delete=models.CASCADE)
    product =   models.CharField(max_length=200)
    image =     models.ImageField(upload_to="product_images/order_img")
    quantity =  models.CharField(max_length=20)
    price =     models.CharField(max_length=200)
    total =     models.CharField(max_length=1000)

    def __str__(self):
        return self.order.user.username
    

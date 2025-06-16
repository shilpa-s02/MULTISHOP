from django.db import models

# class Product(models.Model):
#     product_image = models.ImageField(upload_to='products/')
#     product_name = models.CharField(max_length=100)
#     product_brand = models.CharField(max_length=100)
#     product_category = models.CharField(max_length=100)
#     product_price = models.FloatField()
#     product_quantity = models.IntegerField(default=1)
#     product_description = models.CharField(max_length=500)


#     def __str__(self):
#         return self.product_name

class products(models.Model):
    productName=models.CharField(max_length=100)
    description=models.TextField(max_length=150)
    category=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    tag=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    comparePrice=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    cost=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    sku=models.CharField(max_length=100,unique=True)
    option=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)
    priceAdjustment=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    image=models.ImageField(upload_to='products/',null=True)
    weight=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    dimensions=models.CharField(max_length=100,null=True)
    isActive=models.BooleanField(default=True)
    
class ModelRegister(models.Model):
    businessName=models.CharField( max_length=100)
    ownerName=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.TextField(max_length=200)
    businessType=models.CharField(max_length=100)
    taxId=models.CharField(max_length=50)
    password=models.CharField(max_length=100)


    def __str__(self):
        return self.businessName

# Create your models here.

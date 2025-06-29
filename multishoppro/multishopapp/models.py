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

class Checkout(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    create_account = models.BooleanField(default=False)
    ship_to_different = models.BooleanField(default=False)
    # Shipping address fields
    shipping_first_name = models.CharField(max_length=100, blank=True)
    shipping_last_name = models.CharField(max_length=100, blank=True)
    shipping_email = models.EmailField(blank=True)
    shipping_mobile = models.CharField(max_length=20, blank=True)
    shipping_address1 = models.CharField(max_length=255, blank=True)
    shipping_address2 = models.CharField(max_length=255, blank=True)
    shipping_country = models.CharField(max_length=100, blank=True)
    shipping_city = models.CharField(max_length=100, blank=True)
    shipping_state = models.CharField(max_length=100, blank=True)
    shipping_zip_code = models.CharField(max_length=20, blank=True)
    payment_method = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
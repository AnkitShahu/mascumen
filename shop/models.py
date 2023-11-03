from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class ProductDetails(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique= True, null= True, blank=True)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField()
    product_details = models.TextField(blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(ProductDetails, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.product_name
    


class Img(models.Model):
    category = models.ForeignKey(ProductDetails, on_delete=models.CASCADE, related_name="product_image" )
    image = models.ImageField(upload_to='product_imag/', null=True, blank=True)
    alt = models.CharField(max_length=25, blank=True)

# class UserDetails(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)

    
# class CartViews(models.Model):
#     user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)



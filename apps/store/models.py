from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, blank=True,null=True, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, blank=True,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        

variation_type_choice = (
    ('color', 'color'),
    # ('talla', 'talla'),
)

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_type = models.CharField(max_length=100, choices=variation_type_choice)
    variation_value = models.CharField(max_length=25) # color_name or size
    stock = models.IntegerField()


    def __str__(self):
        return self.product.name + " " + self.variation_type + ' : ' + self.variation_value


class VariantGalery(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name="variant_gallery" )
    

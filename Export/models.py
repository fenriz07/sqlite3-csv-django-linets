from django.db import models

# Create your models here.

class Products(models.Model):


    name = models.TextField()
    sku  = models.TextField( primary_key=True )
    model = models.TextField()
    attribute_color = models.TextField()

    class Meta:
        
        db_table = "master_products_configurable"


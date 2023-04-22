from django.db import models

# Create your models here.

class PricingConfig(models.Model):
    distance_base_price=models.IntegerField(default=0)
    distance_additional_price= models.IntegerField(default=1)
    time_multiplier_factor=models.IntegerField(default=1)
    enable=models.BooleanField(default=False)
    distance_limit = models.DecimalField(max_digits=5, decimal_places=2,default=0) # Add this field
    time_limit = models.IntegerField(default=0)

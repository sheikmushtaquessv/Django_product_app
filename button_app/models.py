from django.db import models

# Create your models here.
class s(models.Model):
    
    ProductName=models.CharField(max_length=100,null=False,blank=False)
    Prices=models.DecimalField(max_digits=10, decimal_places=2)
    Description=models.CharField(max_length=100,null=True,blank=True)
    NumberofReviews=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return self.ProductName   
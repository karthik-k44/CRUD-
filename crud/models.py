from django.db import models

# Create your models here.
class Mobiles(models.Model):
    Name = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    Company =models.CharField(max_length=200)
    Image = models.ImageField(upload_to="Images",null=True)
    
    def __str__(self):
        return f"{self.Name},{self.Price},{self.Company}"
    

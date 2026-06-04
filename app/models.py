from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=255, )
    nationality = models.CharField(max_length=255)
    history = models.TextField()
    has_founded = models.DateField()
    
    def __str__(self):
        return f"{self.brand_name}"
    
class Car(models.Model):
    model_name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    horsepower = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model_name}"
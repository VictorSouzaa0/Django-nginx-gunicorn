from django.db import models
    

class Sector(models.Model):
    sector_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.sector_name}"
    
class Manager(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Employee(models.Model):
    first_name = models.CharField(max_length=255, )
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    about_me = models.TextField()
    joined_at = models.DateField(auto_now=True)
    partner = models.ForeignKey(Manager, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name}"
    
class Team(models.Model):
    team_name = models.IntegerField()
    division = models.CharField(max_length=255)
    partner = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def __str__(self):
       return f"{self.team_name}"
from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
    
class About_Game(models.Model):
    title = models.CharField(max_length=255)
    images = models.URLField(blank=False, null=False)
    video = models.URLField()
    about_game = models.CharField(max_length=2000)
    price = models.FloatField()
    download_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    update_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title    
    
    
    
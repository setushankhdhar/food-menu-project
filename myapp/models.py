from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 
from .managers import ItemManagers
# Create your models here.

class Item(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['food_name','food_price'])
        ]
    def __str__(self):
        
        return self.food_name

    def get_absolute_url(self):
        return reverse("myapp:index")

    objects = ItemManagers()
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    food_name = models.CharField(max_length=100, db_index=True)
    food_desc = models.CharField()
    food_price = models.IntegerField(db_index=True)
    food_image = models.URLField(default='https://metropizza.com.au/wp-content/uploads/2023/06/food-placeholder.jpeg')
    created_at = models.DateField( auto_now_add=True)
    is_available = models.BooleanField(default=True)
    
    
    
    
    
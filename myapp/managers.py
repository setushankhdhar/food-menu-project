from django.db import models
class ItemManagers(models.Manager):
    def cheapItem(self):
        return self.filter(food_price__lt=100)
    def expensiveItem(self):
        return self.filter(food_price__gt=100)
    def search(self,keyword):
        return self.filter(food_name__icontains=keyword)


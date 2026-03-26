from django import forms
from . models import Item
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['food_name','food_desc','food_price','food_image']
        
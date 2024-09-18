from django import forms  
from main.models import ItemEntry  

class ItemForm(forms.ModelForm):  # This should be from 'forms.ModelForm'
    class Meta:
        model = ItemEntry
        fields = ['nama_item', 'harga', 'deskripsi']  # Include your model fields here

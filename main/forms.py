from django import forms  
from main.models import ItemEntry  

class ItemForm(forms.ModelForm):  # This should be from 'forms.ModelForm'
    class Meta:
        model = ItemEntry
        fields = ['nama_item', 'harga', 'deskripsi', 'size', 'warna', 'jumlah']  # Include your model fields here

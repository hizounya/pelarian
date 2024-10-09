from django import forms  
from main.models import ItemEntry
from django.utils.html import strip_tags

class ItemForm(forms.ModelForm):  # This should be from 'forms.ModelForm'
    class Meta:
        model = ItemEntry
        fields = ['nama_item', 'harga', 'deskripsi', 'size', 'warna', 'jumlah']  # Include your model fields here

    def clean_nama_item(self):
        nama_item = self.cleaned_data["nama_item"]
        # Remove any HTML tags to ensure clean input
        return strip_tags(nama_item)

    def clean_deskripsi(self):
        deskripsi = self.cleaned_data["deskripsi"]
        # Remove any HTML tags to ensure clean input
        return strip_tags(deskripsi)

    def clean_harga(self):
        harga = self.cleaned_data["harga"]
        # Ensure the price is a positive value
        if harga < 0:
            raise forms.ValidationError("Harga cannot be negative.")
        return harga
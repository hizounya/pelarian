from django.contrib.auth.models import User
from django.db import models

class ItemEntry(models.Model):
    nama_item = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()
    size = models.CharField(max_length=50, null=True, blank=True)
    warna = models.CharField(max_length=50, null=True, blank=True)
    jumlah = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this field

    def __str__(self):
        return self.nama_item

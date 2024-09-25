from django.db import models
import uuid 
from django.contrib.auth.models import User


class ItemEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_item = models.CharField(max_length=100)
    harga = models.IntegerField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_item
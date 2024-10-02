# Generated by Django 5.1.1 on 2024-10-01 15:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_itementry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itementry',
            name='harga',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='itementry',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

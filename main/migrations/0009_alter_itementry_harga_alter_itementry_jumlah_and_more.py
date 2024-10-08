# Generated by Django 5.1.1 on 2024-10-02 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_itementry_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itementry',
            name='harga',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='itementry',
            name='jumlah',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='itementry',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='itementry',
            name='warna',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

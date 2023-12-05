# Generated by Django 4.2.7 on 2023-12-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreManager', '0008_ordine_carrelloprodotto_ordine'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordine',
            name='prodotti',
            field=models.ManyToManyField(related_name='ordini', through='StoreManager.CarrelloProdotto', to='StoreManager.prodotto'),
        ),
    ]

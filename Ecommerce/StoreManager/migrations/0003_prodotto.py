# Generated by Django 4.2.7 on 2023-11-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreManager', '0002_utente_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodotto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_prodotto', models.CharField(max_length=100)),
                ('tipologia', models.CharField(max_length=20)),
                ('descrizione', models.CharField(max_length=150)),
                ('prezzo', models.FloatField(default=0.0)),
                ('quantita', models.IntegerField(default=0)),
            ],
        ),
    ]

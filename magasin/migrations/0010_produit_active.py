# Generated by Django 5.0.2 on 2024-05-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0009_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-06 20:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(default='', max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('mis_a_jour_le', models.DateTimeField(auto_now=True)),
                ('contenu', models.TextField(default='')),
                ('créé_le', models.DateTimeField(default=django.utils.timezone.now)),
                ('statut', models.IntegerField(choices=[(0, 'Brouillon'), (1, 'Publié')], default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('auteur', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-créé_le'],
            },
        ),
    ]

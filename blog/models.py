from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils import timezone

STATUS_CHOICES = (
    (0, "Brouillon"),
    (1, "Publié")
)

class Post(models.Model):
    titre = models.CharField(max_length=200, unique=True, default='')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', default=None)
    mis_a_jour_le = models.DateTimeField(auto_now=True)
    contenu = models.TextField(default='')
    créé_le = models.DateTimeField(default=timezone.now)
    statut = models.IntegerField(choices=STATUS_CHOICES, default=0)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    class Meta:
        ordering = ['-créé_le']

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

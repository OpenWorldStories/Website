from django.db import models

# Create your models here.
class Worlds(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.slug
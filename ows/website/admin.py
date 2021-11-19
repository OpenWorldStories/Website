from django.contrib import admin

# Register your models here.
from .models import worlds
admin.site.register(worlds.Worlds)

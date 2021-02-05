from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Server, Team, System

admin.site.register(Team)
admin.site.register(System)
admin.site.register(Server)

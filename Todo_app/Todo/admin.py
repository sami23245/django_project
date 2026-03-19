from django.contrib import admin
from Todo import models
from .models import Todo

# Register your models here.

admin.site.register(Todo)
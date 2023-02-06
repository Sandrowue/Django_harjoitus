from django.contrib import admin
from .models import Postaus

# Register your models here.

@admin.register(Postaus)
class PostausAdmin(admin.ModelAdmin):
    list_display = ['otsikko', 'luotu_pvm']
   
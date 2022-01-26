from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "add_date")

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    display = "link"

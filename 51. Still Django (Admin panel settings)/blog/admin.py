from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'status')
    list_filter = ('title', 'author', 'status')
    search_fields = ('title',)

admin.site.register(models.Post, PostAdmin)
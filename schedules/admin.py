from django.contrib import admin
from .models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'link', 'time')

admin.site.register(News, NewsAdmin)
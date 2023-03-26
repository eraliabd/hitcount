from django.contrib import admin
from .models import HitCount, Article


class HitCountAdmin(admin.ModelAdmin):
    list_display = ('url', 'hits')


admin.site.register(HitCount)
admin.site.register(Article)

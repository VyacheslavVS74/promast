from django.contrib import admin
from .models import Works, Top


class WorksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'image_1')
    list_display_links = ('id', 'title')
    search_fields = ('title__iregex', 'description__iregex')


class TopAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name__iregex',)


admin.site.register(Works, WorksAdmin)
admin.site.register(Top, TopAdmin)

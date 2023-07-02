from django.contrib import admin
from .models import Blog, Category, Review
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring import mark_safe


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'cat', 'time_created', 'get_html_image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title__iregex', 'content__iregex')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')
    save_on_top = True
    fields = ('title', 'slug', 'cat', 'content', 'image', 'get_html_image', 'is_published', 'time_created',
              'time_update')
    readonly_fields = ('get_html_image', 'time_created', 'time_update')

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="60">')

    get_html_image.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name__iregex',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)

admin.site.site_title = 'Админ панель ProMast'
admin.site.site_header = 'Админ панель ProMast'

from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    extra = 0
    readonly_fields = ('comment_dt',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_works', 'order_name', 'order_phone', 'order_status', 'order_dt')
    list_display_links = ('id', 'order_works')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt', 'order_works__title')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')
    inlines = [Comment]


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)

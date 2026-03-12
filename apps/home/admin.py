from django.contrib import admin
from .models import Gallery  # Sửa import

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['title', 'description']
    list_filter = ['created_at']
    fieldsets = (
        ('Thông tin hình ảnh', {
            'fields': ('title', 'description', 'image')
        }),
        ('Sắp xếp', {
            'fields': ('order',)
        }),
    )
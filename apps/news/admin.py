from django.contrib import admin
from django.utils.html import format_html
from .models import Category, News, Service, Contact, Gallery

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'location', 'views', 'is_featured', 'is_published', 'created_at']
    list_filter = ['category', 'is_featured', 'is_published', 'location']
    search_fields = ['title', 'summary', 'content']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views']
    fieldsets = (
        ('Thông tin chính', {
            'fields': ('title', 'slug', 'category', 'location')
        }),
        ('Nội dung', {
            'fields': ('image', 'summary', 'content')
        }),
        ('Trạng thái', {
            'fields': ('is_featured', 'is_published', 'views', 'created_at')
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'phone', 'email', 'message']
    readonly_fields = ['created_at']
    actions = ['mark_as_read']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Đánh dấu đã xem"

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['title', 'description']
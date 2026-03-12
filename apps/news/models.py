from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Tên danh mục')
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name='Mô tả')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Danh mục'
        verbose_name_plural = 'Danh mục'
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Tiêu đề')
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Danh mục')
    image = models.ImageField(upload_to='news/%Y/%m/', verbose_name='Ảnh đại diện')
    summary = models.TextField(max_length=500, verbose_name='Tóm tắt')
    content = RichTextField(verbose_name='Nội dung')
    location = models.CharField(max_length=100, blank=True, verbose_name='Địa điểm')
    views = models.IntegerField(default=0, verbose_name='Lượt xem')
    is_featured = models.BooleanField(default=False, verbose_name='Tin nổi bật')
    is_published = models.BooleanField(default=True, verbose_name='Đăng tin')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Ngày đăng')
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Tin tức'
        verbose_name_plural = 'Tin tức'
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Tên dịch vụ')
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(max_length=50, help_text='Font Awesome icon class', verbose_name='Icon')
    description = models.TextField(verbose_name='Mô tả ngắn')
    image = models.ImageField(upload_to='services/', verbose_name='Hình ảnh')
    order = models.IntegerField(default=0, verbose_name='Thứ tự')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Dịch vụ'
        verbose_name_plural = 'Dịch vụ'
        ordering = ['order']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Họ tên')
    phone = models.CharField(max_length=15, verbose_name='Số điện thoại')
    email = models.EmailField(blank=True, verbose_name='Email')
    address = models.CharField(max_length=200, blank=True, verbose_name='Địa chỉ')
    message = models.TextField(verbose_name='Nội dung')
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name='Đã xem')
    
    class Meta:
        verbose_name = 'Liên hệ'
        verbose_name_plural = 'Liên hệ'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.phone}'

# THÊM MODEL GALLERY VÀO ĐÂY
class Gallery(models.Model):
    title = models.CharField(max_length=100, verbose_name='Tiêu đề')
    image = models.ImageField(upload_to='gallery/%Y/%m/', verbose_name='Hình ảnh')
    description = models.CharField(max_length=200, blank=True, verbose_name='Mô tả')
    order = models.IntegerField(default=0, verbose_name='Thứ tự')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Thư viện ảnh'
        verbose_name_plural = 'Thư viện ảnh'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
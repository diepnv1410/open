from django.db import models

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
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
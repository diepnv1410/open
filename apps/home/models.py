from django.db import models

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
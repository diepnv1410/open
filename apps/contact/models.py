from django.db import models

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
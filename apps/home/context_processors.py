from django.conf import settings

def site_settings(request):
    return {
        'site_name': getattr(settings, 'SITE_NAME', 'Phế Liệu Thiệp Nhung'),
        'site_phone': getattr(settings, 'SITE_PHONE', '036.657.9937'),
        'site_email': getattr(settings, 'SITE_EMAIL', 'thiep2k3@gmail.com'),
        'site_address': getattr(settings, 'SITE_ADDRESS', 'KCN Bá Thiện 2, Thiện Kế, Bình Xuyên, Vĩnh Phúc'),
        'site_zalo': getattr(settings, 'SITE_ZALO', '036.657.9937'),
    }
from django.shortcuts import render
from apps.news.models import News, Service, Gallery

def index(request):
    # Get latest news
    latest_news = News.objects.filter(is_published=True)[:3]
    
    # Get featured services
    services = Service.objects.filter(is_active=True)[:6]
    
    # Get gallery images
    gallery = Gallery.objects.all()[:12]
    
    context = {
        'latest_news': latest_news,
        'services': services,
        'gallery': gallery,
        'page_title': 'Trang chủ - Phế Liệu Thiệp Nhung',
    }
    return render(request, 'home/index.html', context)

def about(request):
    context = {
        'page_title': 'Giới thiệu - Phế Liệu Thiệp Nhung',
    }
    return render(request, 'home/about.html', context)

def services(request):
    services = Service.objects.filter(is_active=True)
    context = {
        'services': services,
        'page_title': 'Dịch vụ - Phế Liệu Thiệp Nhung',
    }
    return render(request, 'home/services.html', context)

def picture(request):
    gallery = Gallery.objects.all()
    context = {
        'picture': picture,
        'page_title': 'Hình ảnh - Phế Liệu Thiệp Nhung',
    }
    return render(request, 'home/picture.html', context)

def process(request):
    context = {
        'page_title': 'Quy trình thu mua - Phế Liệu Thiệp Nhung',
    }
    return render(request, 'home/process.html', context)

def maps(request):
    context = {
        'page_title': 'Bản đồ - Phế Liệu Thiệp Nhung',
    }
    return render(request, 'home/maps.html', context)
from django.shortcuts import render, get_object_or_404
from apps.news.models import Service


def service_list(request):
    services = Service.objects.filter(is_active=True)

    context = {
        'services': services,
        'page_title': 'Dịch vụ thu mua - Phế Liệu Thiệp Nhung',
    }

    return render(request, 'services/service_list.html', context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)

    other_services = Service.objects.filter(is_active=True).exclude(id=service.id)[:4]

    context = {
        'service': service,
        'other_services': other_services,
        'page_title': f'{service.name} - Phế Liệu Thiệp Nhung',
    }

    return render(request, 'services/service_detail.html', context)
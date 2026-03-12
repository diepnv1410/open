from apps.news.models import Service

def services_menu(request):
    services = Service.objects.filter(is_active=True).order_by('order')
    return {
        'services_menu': services
    }
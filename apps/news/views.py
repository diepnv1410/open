from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Category

def news_list(request):
    news_list = News.objects.filter(is_published=True)
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        news_list = news_list.filter(category=category)
    
    # Search
    query = request.GET.get('q')
    if query:
        news_list = news_list.filter(title__icontains=query) | news_list.filter(summary__icontains=query)
    
    # Pagination
    paginator = Paginator(news_list, 9)  # 9 news per page
    page = request.GET.get('page')
    news = paginator.get_page(page)
    
    # Get featured news
    featured_news = News.objects.filter(is_featured=True, is_published=True)[:3]
    
    # Get categories with count
    categories = Category.objects.annotate(news_count=models.Count('news'))
    
    context = {
        'news': news,
        'featured_news': featured_news,
        'categories': categories,
        'current_category': category_slug,
        'query': query,
    }
    return render(request, 'news/news_list.html', context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, is_published=True)
    
    # Increment views
    news.views += 1
    news.save(update_fields=['views'])
    
    # Get related news
    related_news = News.objects.filter(
        category=news.category, 
        is_published=True
    ).exclude(id=news.id)[:4]
    
    # Get latest news
    latest_news = News.objects.filter(is_published=True).exclude(id=news.id)[:5]
    
    context = {
        'news': news,
        'related_news': related_news,
        'latest_news': latest_news,
    }
    return render(request, 'news/news_detail.html', context)
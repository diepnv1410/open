from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('gioi-thieu/', views.about, name='about'),
    path('dich-vu/', views.services, name='services'),
    path('quy-trinh-thu-mua/', views.process, name='process'),
    path('khu-vuc-thu-mua/', views.maps, name='maps'),
    path('hinh-anh/', views.picture, name='picture'),   
]
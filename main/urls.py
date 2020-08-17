from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_list_view, name='blog_list_view'),
    path('blog/<str:slug>/', views.blog_detail_view, name='blog_detail_view'),
    path('blog/<str:slug>/edit/', views.blog_update_view, name='blog_update_view'),
    path('blog/<str:slug>/delete/', views.blog_delete_view, name='blog_delete_view'),
    path('blog-new/', views.blog_create_view, name='blog_create_view'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug>', views.single_post, name='post'),
    path('search-result', views.search_result, name='search_result'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('categories', views.categories, name='categories')
]

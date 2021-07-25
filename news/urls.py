from django.urls import path, include
from .views import index, get_category, get_view, add_news

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>', get_view, name='get_view'),
    path('news/add_news', add_news, name="add_news"),

]

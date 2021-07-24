from django.urls import path, include
from .views import index, get_category, get_view

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('new/<int:news_id>', get_view, name='get_view'),

]

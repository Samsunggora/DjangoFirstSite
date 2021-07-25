from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Category
from .forms import New_forms


def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'news list', })


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'title': 'news list', })


def get_view(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        pass
    else:
        form = New_forms()
    return render(request, 'news/add_news.html', {'form': form})

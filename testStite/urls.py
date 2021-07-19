from django.contrib import admin
from django.urls import path
from news.views import index, test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', index),
    path('test/', test),

]

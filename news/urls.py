from django.urls import path, include
from .views import index, test

urlpatterns = [
    path('', index),
    path('test/', test),

]

from django.urls import path
from django.contrib import admin
from blog.views import index

app_name = 'blog'

urlpatterns = [
    path('', index, name='index')
]
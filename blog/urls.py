from django.urls import path
from django.contrib import admin
from blog.views import PostListView, page, post, created_by,category,tag,search

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='PostListView'),
    path('page/<slug:slug>/', page, name='page'),
    path('post/<slug:slug>/', post, name='post'),
    path('created_by/<int:author_pk>/', created_by, name='created_by'),
    path('category/<slug:slug>/', category, name='category'),
    path('tag/<slug:slug>/', tag, name='tag'),
    path('search/', search, name='search')
]
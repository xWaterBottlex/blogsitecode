from django.urls import path, include
from . import views
from .views import (PostListView, PostDetailView, 
                    PostCreateView, PostUpdateView, 
                    PostDeleteView, UserPostListView, api_info)


urlpatterns = [
    path('', views.home, name='guitar-lovers-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('forums/', PostListView.as_view(), name='guitar-lovers-fourms'),
    path('forums/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('forums/new/', PostCreateView.as_view(), name='post-new'),
    path('forums/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('forums/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('api/info', api_info, name='api-info')
]
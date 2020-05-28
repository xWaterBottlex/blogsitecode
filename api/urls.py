from django.urls import path
from .views import BlogPostRudView, BlogPostApiView


urlpatterns = [
    path('<int:pk>/', BlogPostRudView.as_view(), name='post-rud'),
    path('', BlogPostApiView.as_view(), name='apis')
]
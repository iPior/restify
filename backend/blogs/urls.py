
from django.contrib import admin
from django.urls import include, path

from blogs.views import BlogFeed, BlogView, BlogLikeView

urlpatterns = [
    path('feed/', BlogFeed.as_view()),
    path('<int:id>/', BlogView.as_view()),
    path('<int:id>/like/', BlogLikeView.as_view()),
]

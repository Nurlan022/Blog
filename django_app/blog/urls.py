from django.contrib import admin
from django.urls import path
from . import views

from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView,
	CategoryView,
	LikeView,
	CommentView,
	AddCommentLike,
	CommentReplyView,
	)


urlpatterns = [
    path('', PostListView.as_view(),name="blog-home"),

    path('user/<str:username>', UserPostListView.as_view(),name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(),name="post_detail"),
    path('comment/<int:pk>', CommentView,name="comment_post"),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment_like'),
    path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment_reply'),
    path('category/<str:cats>/', CategoryView,name="category"),
    path('like/<int:pk>', LikeView,name="like_post"),
    path('post/new/', PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name="post-delete"),
    path('about/', views.about,name="blog-about"),
]

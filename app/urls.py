from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDeleteView
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('api/posts/', PostListCreateView.as_view(), name='post_list_create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post_detail_update_delete'),
]

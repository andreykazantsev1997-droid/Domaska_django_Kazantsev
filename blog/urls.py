from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete')

]
from django.urls import path
from .views import PostListCreate, PostRetrieveUpdateDestroy

urlpatterns = [
    path('post/', PostListCreate.as_view(), name='post-list-create'),
    path('post/<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post-detail'),
]

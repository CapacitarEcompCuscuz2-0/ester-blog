from django.urls import path
from posts.views import index, PostListView, PostUpdateView, PostDetailView

app_name = 'posts'

urlpatterns = [
    path("", index, name="index"),
    path("allposts", PostListView.as_view(), name="allposts"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="detail"),
]
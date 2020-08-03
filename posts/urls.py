from django.urls import path
from posts.views import index, PostListView, PostDeleteView, PostUpdateView, PostDetailView, PostCreateView

app_name = 'posts'

urlpatterns = [
    path("", index, name="index"),
    path("allposts", PostListView.as_view(), name="allposts"),
    path("deletepost/<int:pk>/", PostDeleteView.as_view(), name="deletepost"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("create", PostCreateView.as_view(), name="create"),
]
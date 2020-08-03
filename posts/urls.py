from django.urls import path
from posts.views import index, PostListView, PostDeleteView

app_name = 'posts'

urlpatterns = [
    path("", index, name="index"),
    path("allposts", PostListView.as_view(), name="allposts"),
    path("deletepost/<int:pk>/", PostDeleteView.as_view(), name="deletepost"),
]
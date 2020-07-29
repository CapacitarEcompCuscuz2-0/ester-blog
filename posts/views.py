from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Post

# Create your views here.

def index(request):
    context = {
        'hello' : 'hello',
    }
    return render(request, 'posts/index.html', context)

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/allposts.html'
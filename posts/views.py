from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from posts.models import Post
from django.urls import reverse_lazy

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

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'posts/update.html'
    success_url = reverse_lazy('posts:allposts')
    fields = ['title', 'text']

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/detail.html'
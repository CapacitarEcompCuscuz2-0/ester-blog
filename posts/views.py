from django.shortcuts import render
from django.views import generic
from posts.models import Post
from posts.forms import PostCreateForm
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    context = {
        'hello' : 'hello',
    }
    return render(request, 'posts/index.html', context)

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/allposts.html'

class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'posts/createapost.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('posts:allposts')
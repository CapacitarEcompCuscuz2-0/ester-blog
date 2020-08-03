from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from posts.models import Post

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
    context_object_name = 'posts'
    template_name = 'posts/createpost.html'
    success_url = reverse_lazy('posts:allposts')
    fields = ['title', 'text']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/deletepost.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('posts:allposts')

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'posts/update.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:allposts')
    fields = ['title', 'text']

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/detail.html' 
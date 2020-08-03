from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import views
from users.models import User
from users.forms import UserSignupForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserListView(generic.ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'

class UserDetailView(generic.DetailView):
    model = User
    context_object_name = 'users'
    template_name = 'users/list.html'

class UserLoginView(views.LoginView):
    template_name = 'users/login.html'

class UserSignupView(generic.CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('posts:allposts')

class UserLogoutView(LoginRequiredMixin, views.LogoutView):
    pass 
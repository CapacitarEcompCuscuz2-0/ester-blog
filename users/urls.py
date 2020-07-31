from django.urls import path
from users.views import UserLoginView, UserDetailView, UserListView, UserSignupView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('signup', UserSignupView.as_view(), name='signup'),
    path('logout', UserLogoutView.as_view(), name="logout"),
]

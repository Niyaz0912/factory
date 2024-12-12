from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileView, UserListView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='create_user'),
    path('login/', UserLoginView.as_view(), name='login_user'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('update/', UserLogoutView.as_view(), name='update'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('users/', UserListView.as_view(), name='user_list'),
]

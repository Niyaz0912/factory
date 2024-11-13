from django.urls import path
from .views import UserCreateView, UserLoginView, UserLogoutView, UserProfileView, UserListView

app_name = 'users'

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='create_user'),  # Страница создания пользователя
    path('login/', UserLoginView.as_view(), name='login'),  # Страница входа
    path('logout/', UserLogoutView.as_view(), name='logout'),  # Страница выхода
    path('profile_user/', UserProfileView.as_view(), name='profile'),  # Страница профиля пользователя
    path('user_list/', UserListView.as_view(), name='user_list'),  # Страница списка пользователей
]
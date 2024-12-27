from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileView, UserListView, UserUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='create_user'),
    path('login/', UserLoginView.as_view(), name='login_user'),  # Обратите внимание на имя здесь
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),  # Обновление пользователя
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),  # Профиль пользователя
    path('users/', UserListView.as_view(), name='user_list'),  # Список пользователей
]

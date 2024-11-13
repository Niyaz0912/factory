from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

User = get_user_model()


class UserCreateView(View):
    def get(self, request):
        return render(request, 'users/create_user.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверка на существование пользователя с таким же именем
        if User.objects.filter(username=username).exists():
            error_message = "Пользователь с таким именем уже существует."
            return render(request, 'users/create_user.html', {'error_message': error_message})

        # Создаем пользователя с хэшированным паролем
        user = User(username=username, password=make_password(password))
        user.save()

        return redirect('process_history:login')  # Перенаправление на страницу входа после создания пользователя


User = get_user_model()  # Получаем текущую модель пользователя


class UserLoginView(TemplateView):
    template_name = 'users/login.html'  # Убедитесь, что путь к шаблону правильный

    def get(self, request, *args, **kwargs):
        # Получаем всех пользователей для отображения на странице входа
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('process_history:shift_assignment')  # Перенаправление на страницу сменных заданий
        else:
            error_message = "Неверное имя пользователя или пароль."
            users = User.objects.all()  # Получаем всех пользователей для отображения на странице входа
            return render(request, self.template_name, {'error_message': error_message, 'users': users})


class UserLogoutView(View):
    def get(self, request):
        logout(request)  # Выход пользователя
        return redirect('users:login')  # Перенаправление на страницу входа после выхода


class UserProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'users/profile_user.html', {'user': request.user})
        else:
            return redirect('process_history:login')


class UserListView(View):
    def get(self, request):
        users = User.objects.all()  # Получаем всех пользователей
        return render(request, 'users/user_list.html', {'users': users})

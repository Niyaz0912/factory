# users/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

User = get_user_model()


class UserCreateView(View):
    def get(self, request):
        return render(request, 'registration/create_user.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверка на существование пользователя с таким же именем
        if User.objects.filter(username=username).exists():
            error_message = "Пользователь с таким именем уже существует."
            return render(request, 'registration/create_user.html', {'error_message': error_message})

        # Создаем пользователя с хэшированным паролем
        user = User(username=username, password=make_password(password))
        user.save()

        return redirect('process_history:login')  # Перенаправление на страницу входа после создания пользователя


class UserLoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('process_history:shift_assignment')  # Перенаправление на страницу сменных заданий
        else:
            error_message = "Пароль неверный!"  # Сообщение об ошибке
            return render(request, 'registration/login.html', {
                'error_message': error_message,
                'username': username  # Сохраняем выбранное имя пользователя для удобства
            })


class UserLogoutView(View):
    def get(self, request):
        logout(request)  # Выход пользователя
        return redirect('process_history:login')  # Перенаправление на страницу входа после выхода


class UserProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'registration/profile.html', {'user': request.user})
        else:
            return redirect('process_history:login')


class UserListView(View):
    def get(self, request):
        users = User.objects.all()  # Получаем всех пользователей
        return render(request, 'registration/user_list.html', {'users': users})
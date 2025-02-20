from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from django.urls import reverse_lazy
from users.models import User, UserRoles
from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm, UserForm

from shift_assignment.models import ShiftAssignment, CompletedShiftAssignment


class UserRegisterView(CreateView):
    """
    Представление для регистрации нового пользователя.

    Это представление использует форму регистрации и перенаправляет на страницу входа после успешной регистрации.
    """
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login_user')  # Убедитесь, что это имя маршрута соответствует вашему urls.py
    template_name = 'users/register_user.html'


class UserLoginView(LoginView):
    """
    Представление для входа пользователя.

    Это представление проверяет учетные данные пользователя и перенаправляет на профиль после успешного входа.
    """
    form_class = UserLoginForm
    template_name = 'users/login_user.html'

    def form_valid(self, form):
        """Обрабатывает успешное заполнение формы входа."""
        user = form.get_user()
        login(self.request, user)
        return redirect('users:user_profile', pk=user.pk)


class UserProfileView(LoginRequiredMixin, DetailView):
    """
    Представление для отображения профиля пользователя.

    Это представление показывает информацию о пользователе и связанные с ним задания.
    """
    model = User
    template_name = 'users/user_profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Добавляет дополнительные данные в контекст профиля пользователя."""
        context = super().get_context_data(**kwargs)
        user_role = self.request.user.role  # Получаем роль пользователя

        # Устанавливаем can_create_shift для администраторов и мастеров
        context['can_create_shift'] = user_role in [UserRoles.ADMIN, UserRoles.MASTER]

        # Получаем текущие сменные задания в зависимости от роли пользователя
        if user_role in [UserRoles.ADMIN, UserRoles.MASTER]:
            context['shift_assignments'] = ShiftAssignment.objects.all()  # Все задания для админа и мастера
        elif user_role == UserRoles.OPERATOR:
            context['shift_assignments'] = ShiftAssignment.objects.filter(operator=self.request.user)

        # Получаем выполненные сменные задания для текущего пользователя и всех мастеров и администраторов
        if user_role in [UserRoles.ADMIN, UserRoles.MASTER]:
            context[
                'completed_assignments'] = CompletedShiftAssignment.objects.all()  # Все выполненные задания для админа и мастера
        else:
            context['completed_assignments'] = CompletedShiftAssignment.objects.filter(
                operator=self.request.user)  # Только для оператора

        # Передаем строковые значения ролей в контекст
        context['is_admin'] = user_role == UserRoles.ADMIN
        context['is_master'] = user_role == UserRoles.MASTER
        context['is_operator'] = user_role == UserRoles.OPERATOR

        return context


class UserUpdateView(UpdateView):
    """
    Представление для обновления данных пользователя.

    Это представление позволяет пользователю обновить свои данные.
    """
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update_user.html'

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного обновления."""
        return reverse_lazy('users:user_profile', kwargs={'pk': self.object.pk})


class UserLogoutView(LogoutView):
    """
    Представление для выхода пользователя из системы.

    Это представление обрабатывает выход и перенаправляет на страницу входа.
    """

    template_name = 'users/logout_user.html'
    next_page = reverse_lazy('users:login_user')


class UserListView(LoginRequiredMixin, ListView):
    """
    Представление для отображения списка пользователей.

    Это представление показывает всех активных пользователей системы.
    """

    model = User
    extra_context = {
        'title': 'Сотрудники УМКИ:'
    }

    template_name = 'users/users.html'

    def get_queryset(self):
        """Фильтрует список пользователей по активности."""
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)  # Показывает только активных пользователей
        return queryset


class UserViewProfileView(DetailView):
    """
    Представление для просмотра профиля другого пользователя.

    Это представление отображает информацию о выбранном пользователе.
    """

    model = User
    template_name = 'users/user_view_profile.html'

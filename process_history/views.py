from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password
from django.views import View
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.db import IntegrityError

from .models import ShiftAssignment, ProcessHistory
from .forms import ProcessHistoryForm


class HomePageView(TemplateView):
    template_name = 'process_history/home.html'


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

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

    return render(request, 'registration/login.html')  # Отображение формы входа


def logout_view(request):
    logout(request)  # Выход пользователя
    return redirect('process_history:login')  # Перенаправление на страницу входа после выхода


class ShiftAssignmentView(LoginRequiredMixin, TemplateView):
    template_name = 'process_history/shift_assignments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignments'] = ShiftAssignment.objects.filter(operator=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        return redirect('process_history:history_process_create')  # Перенаправление на страницу создания истории процесса


class HistoryProcessCreateView(LoginRequiredMixin, FormView):
    template_name = 'process_history/history_process_create.html'
    form_class = ProcessHistoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignment_id = self.kwargs.get('assignment_id')
        context['assignment'] = ShiftAssignment.objects.get(id=assignment_id)
        return context

    def form_valid(self, form):
        process_history = form.save(commit=False)
        process_history.user = self.request.user
        process_history.assignment = self.get_context_data()['assignment']
        process_history.save()

        # Логика для создания модальных окон для ввода параметров
        # Это может быть реализовано через JavaScript на клиентской стороне

        return super().form_valid(form)


class CompleteProcessHistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'process_history/complete_process_history.html'

    def post(self, request, *args, **kwargs):
        # Логика завершения истории процесса
        return redirect('process_history:shift_assignments_update')


class ShiftAssignmentsUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'process_history/shift_assignments_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignment_id = self.kwargs.get('assignment_id')
        context['assignment'] = ShiftAssignment.objects.get(id=assignment_id)
        return context

    def post(self, request, *args, **kwargs):
        # Логика обновления сменного задания и ввода количества брака
        assignment_id = self.kwargs.get('assignment_id')
        assignment = ShiftAssignment.objects.get(id=assignment_id)

        # Обновление полей задания на основе введенных данных
        assignment.broken_count = request.POST.get('broken_count')
        assignment.save()

        return redirect('process_history:shift_assignments')  # Перенаправление на страницу со сменными заданиями

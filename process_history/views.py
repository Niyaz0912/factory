# class ProcessHistoryListView(ListView):
#     model = ProcessHistory
#     extra_context = {
#         'title': 'Все истории процессов',
#     }
#     template_name = 'process_history/process_history_list.html'  # Убедитесь, что путь к шаблону правильный
#     context_object_name = 'process_histories'  # Имя контекста для шаблона
#
#     def get_queryset(self):
#         return ProcessHistory.objects.all()  # Возвращает все записи
#
#
# class ProcessHistoryCreateView(LoginRequiredMixin, CreateView):
#     model = ProcessHistory
#     extra_context = {
#         'title': 'Создание процесса',
#     }
#     success_url = reverse_lazy('process_history:process_history_create')
#     template_name = 'process_history/process_history.html'
#
#     def form_valid(self, form):
#         if self.request.user.role not in [UserRoles.USER, UserRoles.MASTER]:
#             return HttpResponseForbidden("Нет соответствующего доступа!")
#         self.object = form.save()
#         self.object.user = self.request.user
#         if self.object.detail_quantity == 120:
#             print("Замените инструмент")
#             return reverse('process_history:process_history_change')
#         self.object.save()
#         return super().form_valid(form)
#
#     def get_form_class(self):
#         if self.object.detail_quantity == 0 or self.object.detail_quantity % 150 == 0:
#             process_form_class = ProcessHistoryForm
#         else:
#             process_form_class = ProcessHistoryFormShort
#         return process_form_class
#
#
# class ProcessHistoryDetailView(LoginRequiredMixin, DetailView):
#     model = ProcessHistory
#     extra_context = {
#         'title': 'Подробная информация о процессе',
#     }
#     template_name = 'process_history/process_history_detail'
#
#
# class ProcessHistoryUpdateView(LoginRequiredMixin, UpdateView):
#     model = ProcessHistory
#     form_class = ProcessHistoryForm
#     extra_context = {
#         'title: Внесение изменений в процесс',
#     }
#
#     def get_success_url(self):
#         return reverse('process_history:process_history_detail', args=[self.kwargs.get('pk')])
#
#     def get_object(self, queryset=None):
#         self.object = super().get_object(queryset)
#         if self.request.user.role != UserRoles.MASTER:
#             raise PermissionDenied()
#         reverse(self.object)

from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from .models import ShiftAssignment, ProcessHistory
from .forms import ProcessHistoryForm, ShiftAssignmentForm
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class HomePageView(TemplateView):
    template_name = 'process_history/home.html'  # Убедитесь, что этот шаблон существует


# Заданный пароль для авторизации
AUTH_PASSWORD = "12345678"  # Пример 8-значного пароля


class ShiftAssignmentView(LoginRequiredMixin, TemplateView):
    template_name = 'process_history/shift_assignments.html'

    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            password = request.POST.get('password')
            if password == AUTH_PASSWORD:
                assignments = ShiftAssignment.objects.filter(user=request.user)
                return self.render_to_response({'assignments': assignments})
            else:
                return HttpResponseForbidden("Неверный пароль")
        return render(request, 'process_history/login.html')


class HistoryProcessCreateView(LoginRequiredMixin, FormView):
    template_name = 'process_history/history_process_create.html'
    form_class = ProcessHistoryForm
    success_url = reverse_lazy('process_history:history_process_create')

    def form_valid(self, form):
        process_history = form.save(commit=False)
        process_history.user = self.request.user
        process_history.save()
        return super().form_valid(form)


class CompleteProcessHistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'process_history/complete_process_history.html'

    def post(self, request, *args, **kwargs):
        # Логика завершения истории процесса
        # Сохранение данных в БД и перенаправление на страницу обновления задания
        return redirect('process_history:shift_assignments_update')


class ShiftAssignmentsUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'process_history/shift_assignments_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignments'] = ShiftAssignment.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        # Логика обновления сменного задания
        # Сохранение изменений в БД и перенаправление на страницу со сменными заданиями
        return redirect('process_history:shift_assignments')


def login_view(request):
    if request.method == 'POST':
        # Получаем данные из формы
        username = request.POST.get('username')  # Имя пользователя (или ФИО)
        password = request.POST.get('password')  # Пароль

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Вход в систему
            return redirect('home')  # Перенаправление на главную страницу или другую страницу
        else:
            error_message = "Неверное имя пользователя или пароль."
            return render(request, 'registration/login.html', {'error_message': error_message})

    return render(request, 'registration/login.html')  # Отображение формы входа

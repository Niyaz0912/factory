from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from shift_assignment.models import ShiftAssignment
from .forms import ProcessHistoryForm
from .models import ProcessHistory
from users.models import UserRoles


class HomePageView(TemplateView):
    template_name = 'process_history/home.html'


class HistoryProcessCreateView(LoginRequiredMixin, CreateView):
    model = ProcessHistory
    template_name = 'process_history/history_process_create.html'
    form_class = ProcessHistoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignment_id = self.kwargs.get('assignment_id')
        context['assignment'] = ShiftAssignment.objects.get(id=assignment_id)
        return context

    def form_valid(self, form):
        process_history = form.save()
        if self.request.user.role not in [UserRoles.MASTER, UserRoles.ADMIN, UserRoles.OPERATOR]:
            raise PermissionDenied()
        process_history.user = self.request.user
        process_history.save()

        return super().form_valid(form)


def save_process_history(request):
    if request.method == 'POST':
        # Обработка данных формы и сохранение в базу данных
        # Пример:
        control_code = request.POST.get('control_code')
        mark = request.POST.get('mark')
        quantity = request.POST.get('quantity')
        parameters = request.POST.get('parameters')

        # Создание объекта ProcessHistory
        process_history = ProcessHistory(
            control_code=control_code,
            mark=mark,
            quantity=quantity,
            parameters=parameters,
            user=request.user  # Привязка к текущему пользователю
        )
        process_history.save()

        return redirect('some_view_name')  # Замените на правильное имя маршрута для перенаправления после сохранения
    return render(request, 'process_history/save_process_history.html')
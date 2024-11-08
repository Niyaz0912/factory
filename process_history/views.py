from audioop import reverse
from msilib.schema import ListView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from pandas.core.indexers import check_key_length

from process_history.models import ProcessHistory
from process_history.forms import ProcessHistoryForm, ProcessHistoryFormShort
from users.models import UserRoles
from django.http import HttpResponse


# def process_history_view(request, task_id):
#     if request.method == 'POST':
#         # Обработка данных формы
#         for i in range(1, len(request.POST) // 4 + 1):
#             control_code = request.POST.get(f'control_code_{i}')
#             mark = request.POST.get(f'mark_{i}')
#             quantity = request.POST.get(f'quantity_{i}')
#             param_count = request.POST.get(f'param_count_{i}') == '+'
#
#             # Сохранение данных в базе данных
#             ProcessHistory.objects.create(
#                 task_id=task_id,
#                 control_code=control_code,
#                 mark=mark,
#                 quantity=quantity,
#                 param_count=param_count
#             )
#
#         return redirect('success_page')  # Перенаправление на страницу успеха или другую страницу
#
#     # Получение параметров для отображения на странице
#     parameters = get_parameters_for_task(task_id)  # Реализуйте эту функцию для получения параметров
#     return render(request, 'process_history/process_history.html', {'parameters': parameters})

def index(request):
    return HttpResponse("<h1>Welcome to the Index Page!</h1>")


#
# class ProcessHistoryListView(ListView):
#     model = ProcessHistory
#     extra_context = {
#         'title: Все истории процессов',
#     }
#     template_name = 'process_history/process_history_list.html'

from django.views.generic import ListView
from .models import ProcessHistory


class ProcessHistoryListView(ListView):
    model = ProcessHistory
    template_name = 'process_history/process_history_list.html'  # Убедитесь, что путь к шаблону правильный
    context_object_name = 'process_histories'  # Имя контекста для шаблона

    def get_queryset(self):
        return ProcessHistory.objects.all()  # Возвращает все записи


class ProcessHistoryCreateView(LoginRequiredMixin, CreateView):
    model = ProcessHistory
    extra_context = {
        'title: Создание процесса',
    }
    success_url = reverse_lazy('process_history:process_history_list')
    template_name = 'process_history/process_history.html'

    def form_valid(self, form):
        if self.request.user.role not in [UserRoles.USER, UserRoles.MASTER]:
            return HttpResponseForbidden("Нет соответствующего доступа!")
        self.object = form.save()
        self.object.user = self.request.user
        if self.object.detail_quantity == 120:
            print("Замените инструмент")
            return reverse('process_history:process_history_change')
        self.object.save()
        return super().form_valid(form)

    def get_form_class(self):
        if self.object.detail_quantity == 0 or self.object.detail_quantity % 150 == 0:
            process_form_class = ProcessHistoryForm
        else:
            process_form_class = ProcessHistoryFormShort
        return process_form_class


class ProcessHistoryDetailView(LoginRequiredMixin, DetailView):
    model = ProcessHistory
    extra_context = {
        'title: Подробная информация о процессе',
    }
    template_name = 'process_history/process_history_detail'


class ProcessHistoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProcessHistory
    form_class = ProcessHistoryForm
    extra_context = {
        'title: Внесение изменений в процесс',
    }

    def get_success_url(self):
        return reverse('process_history:process_history_detail', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.role != UserRoles.MASTER:
            raise PermissionDenied()
        reverse(self.object)

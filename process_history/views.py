from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from shift_assignment.models import ShiftAssignment
from django.views import View
from django.http import JsonResponse

from .forms import ProcessHistoryForm
from .models import ProcessHistory
import json

from django.views.generic import TemplateView
from .utils import export_to_excel


class HomePageView(TemplateView):
    template_name = 'process_history/home.html'  # Убедитесь, что у вас есть этот шаблон

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = reverse('users:login_user')  # Используйте правильное имя
        return context


class HistoryProcessCreateView(CreateView):
    model = ProcessHistory
    form_class = ProcessHistoryForm
    template_name = 'process_history/history_process_create.html'
    success_url = '/process_history/'  # URL для перенаправления после успешного создания записи

    def form_valid(self, form):
        # Сначала сохраняем форму
        response = super().form_valid(form)

        # Экспорт данных в Excel после успешного сохранения
        export_to_excel('process_history.xlsx')  # Укажите путь к файлу

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        shift_assignment = get_object_or_404(ShiftAssignment, pk=pk)

        # Передаем данные из сменного задания в контекст
        context['operator'] = shift_assignment.operator.username if shift_assignment.operator else 'Неизвестно'
        context['operation_name'] = shift_assignment.operation_name
        context['machine_id'] = shift_assignment.machine_id
        context['part_id'] = shift_assignment.part_id
        context['batch_number'] = shift_assignment.batch_number

        return context


class SaveProcessHistoryView(LoginRequiredMixin, View):
    def post(self, request):
        try:
            rows = json.loads(request.POST.get('rows'))
            assignment_id = request.POST.get('assignment_id')  # Получаем ID сменного задания
            shift_assignment = get_object_or_404(ShiftAssignment, id=assignment_id)  # Получаем объект сменного задания

            for row in rows:
                ProcessHistory.objects.create(
                    control_code=row['control_code'],
                    mark=row['mark'],
                    quantity=row['quantity'],
                    parameters=row['parameters'],
                    user=request.user,
                    shift_assignment=shift_assignment  # Сохраняем связь с заданием
                )
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

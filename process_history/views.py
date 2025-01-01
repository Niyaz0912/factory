import logging
from django.urls import reverse
from django.views.generic import TemplateView

from shift_assignment.models import ShiftAssignment, CompletedShiftAssignment
from .forms import ProcessHistoryForm, SaveProcessHistoryForm
from .models import ProcessHistory
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

logger = logging.getLogger(__name__)


class HomePageView(TemplateView):
    template_name = 'process_history/home.html'  # Убедитесь, что у вас есть этот шаблон

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = reverse('users:login_user')  # Используйте правильное имя
        return context


class HistoryProcessCreateView(View):
    model = ProcessHistory
    form_class = ProcessHistoryForm
    template_name = 'process_history/history_process_create.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')  # Получаем ID сменного задания из URL
        shift_assignment = get_object_or_404(ShiftAssignment, pk=pk)

        context = {
            'operator': shift_assignment.operator.username if shift_assignment.operator else 'Неизвестно',
            'operation_name': shift_assignment.operation_name,
            'machine_id': shift_assignment.machine_id,
            'part_id': shift_assignment.part_id,
            'batch_number': shift_assignment.batch_number,
            'shift_assignment': shift_assignment,
            'form': ProcessHistoryForm(),
            'process_history': ProcessHistory.objects.filter(user=request.user),
            'assignment_id': pk  # Передаем assignment_id в контекст
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ProcessHistoryForm(request.POST)
        if form.is_valid():
            process_history = form.save(commit=False)
            process_history.user = request.user

            pk = self.kwargs.get('pk')  # Получаем ID сменного задания из URL
            shift_assignment = get_object_or_404(ShiftAssignment, pk=pk)

            process_history.machine_id = shift_assignment.machine_id
            process_history.part_id = shift_assignment.part_id
            process_history.batch_number = shift_assignment.batch_number

            process_history.save()

            return redirect('/process_history/')

        return render(request, self.template_name, {'form': form})


class SaveProcessHistoryView(View):
    model = ProcessHistory
    form_class = SaveProcessHistoryForm
    template_name = 'process_history/save_process_history.html'

    def get(self, request, assignment_id):
        shift_assignment = get_object_or_404(ShiftAssignment, id=assignment_id)
        context = {
            'shift_assignment': shift_assignment,
            'form': ProcessHistoryForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, assignment_id):
        form = ProcessHistoryForm(request.POST)

        if form.is_valid():
            # Создаем новый объект CompletedShiftAssignment
            completed_shift_assignment = CompletedShiftAssignment(
                operator=request.POST.get('operator'),
                operation_name=request.POST.get('operation_name'),
                machine_id=request.POST.get('machine_id'),
                part_id=request.POST.get('part_id'),
                batch_number=request.POST.get('batch_number'),
                quantity=request.POST.get('quantity'),
                defect_quantity=request.POST.get('defect_quantity', 0),  # Дефолтное значение 0
                stop_reason=request.POST.get('stop_reason', 'Работа в нормальном режиме')  # Дефолтное значение
            )

            # Сохраняем запись в базе данных
            completed_shift_assignment.save()

            # Перенаправление на профиль пользователя после сохранения
            return redirect(f'/users/profile/{request.user.id}/')  # Замените на правильный URL для профиля

        return render(request, self.template_name, {'form': form})

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import ShiftAssignmentForm, CompletedShiftAssignmentForm
from .models import ShiftAssignment, CompletedShiftAssignment

import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse


class UploadShiftAssignmentView(LoginRequiredMixin, View):
    """
    Представление для загрузки сменных заданий из Excel файла.

    Это представление обрабатывает загрузку файла и сохранение данных в базу данных.
    """

    template_name = 'shift_assignment/upload_shift_assignment.html'

    def get(self, request):
        """Обрабатывает GET запрос для отображения формы загрузки."""
        return render(request, self.template_name)

    def post(self, request):
        """Обрабатывает POST запрос для загрузки файла с данными."""
        if request.method == 'POST' and 'file' in request.FILES:
            file = request.FILES['file']
            try:
                # Проверка формата файла
                if not file.name.endswith(('.xls', '.xlsx')):
                    return JsonResponse({'status': 'error', 'message': 'Неподдерживаемый формат файла.'})

                # Парсинг Excel файла
                df = pd.read_excel(file)

                # Проверка наличия необходимых столбцов
                required_columns = ['batch_number', 'operation_name', 'quantity', 'operator_id', 'part_id',
                                    'machine_id']
                missing_columns = [col for col in required_columns if col not in df.columns]

                if missing_columns:
                    return JsonResponse({'status': 'error',
                                         'message': f'Отсутствуют обязательные столбцы: {", ".join(missing_columns)}'})

                # Получаем модель пользователя
                User = get_user_model()

                # Логика для сохранения данных из DataFrame в базу данных
                for index, row in df.iterrows():
                    operator_id = row['operator_id']
                    try:
                        operator = User.objects.get(id=operator_id)  # Получите объект пользователя по ID
                    except User.DoesNotExist:
                        return JsonResponse(
                            {'status': 'error', 'message': f'Пользователь с ID {operator_id} не найден.'})

                    ShiftAssignment.objects.create(
                        batch_number=row['batch_number'],
                        operation_name=row['operation_name'],
                        quantity=row['quantity'],
                        operator=operator,
                        part_id=row['part_id'],
                        machine_id=row['machine_id'],
                        date=row['date']  # Убедитесь, что у вас есть значение для даты
                    )

                # Перенаправление на страницу профиля пользователя после успешной загрузки
                return redirect('users:user_profile', pk=request.user.pk)  # Передаем ID текущего пользователя

            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

        return JsonResponse({'status': 'error', 'message': 'Ошибка при загрузке файла.'})


class CompletedShiftAssignmentView(View):
    """
    Представление для создания завершенного сменного задания.

    Это представление отображает форму для завершения задания и обрабатывает его сохранение.
    """

    model = ShiftAssignment  # Указываем модель, если это необходимо
    template_name = 'shift_assignment/completed_shift_assignment.html'

    def get(self, request, *args, **kwargs):
        """Обрабатывает GET запрос для отображения формы завершенного задания."""
        assignment_id = kwargs.get('pk')  # Получаем ID сменного задания из URL
        shift_assignment = get_object_or_404(ShiftAssignment, id=assignment_id)

        # Передаем объект сменного задания в контекст
        initial_data = {
            'operator': shift_assignment.operator,
            'operation_name': shift_assignment.operation_name,
            'machine_id': shift_assignment.machine_id,
            'part_id': shift_assignment.part_id,
            'batch_number': shift_assignment.batch_number,
            'quantity': shift_assignment.quantity,
        }

        context = {
            'form': CompletedShiftAssignmentForm(initial=initial_data),  # Заполняем форму начальными данными
            'shift_assignment': shift_assignment,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """Обрабатывает POST запрос для сохранения завершенного задания."""
        form = CompletedShiftAssignmentForm(request.POST)

        if form.is_valid():
            # Создаем новый объект CompletedShiftAssignment
            completed_shift_assignment = form.save(commit=False)
            completed_shift_assignment.operator = request.user

            # Получаем ID сменного задания и связываем его с завершенным заданием
            assignment_id = kwargs.get('pk')
            shift_assignment = get_object_or_404(ShiftAssignment, id=assignment_id)
            completed_shift_assignment.shift_assignment = shift_assignment

            # Заполняем остальные поля из сменного задания
            completed_shift_assignment.operator = shift_assignment.operator  # Пример поля
            completed_shift_assignment.operation_name = shift_assignment.operation_name
            completed_shift_assignment.machine_id = shift_assignment.machine_id
            completed_shift_assignment.part_id = shift_assignment.part_id
            completed_shift_assignment.batch_number = shift_assignment.batch_number

            # Сохраняем объект выполненного задания в базе данных
            completed_shift_assignment.save()

            # Удаляем исходное сменное задание из базы данных
            shift_assignment.delete()  # Удаляем только ShiftAssignment

            # Перенаправляем на профиль пользователя с его ID
            return redirect('users:user_profile', pk=request.user.pk)  # Используем правильное имя маршрута

        # Если форма не валидна, повторно получаем объект сменного задания для передачи в контекст
        assignment_id = kwargs.get('pk')
        shift_assignment = get_object_or_404(ShiftAssignment, id=assignment_id)

        return render(request, self.template_name, {
            'form': form,
            'shift_assignment': shift_assignment,
        })


class CompletedShiftAssignmentUpdateView(UpdateView):
    """
    Представление для обновления завершенного сменного задания.

    Это представление обрабатывает обновление существующего завершенного задания.
    """

    model = CompletedShiftAssignment
    form_class = CompletedShiftAssignmentForm
    template_name = 'shift_assignment/completed_shift_assignment_update.html'

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного обновления."""
        return reverse_lazy('users:user_profile', kwargs={'pk': self.request.user.pk})


class DeleteCompletedShiftView(View):
    """
    Представление для удаления завершенного сменного задания.

    Это представление обрабатывает удаление существующего завершенного задания.
    """

    def post(self, request, id):
        """Обрабатывает POST запрос для удаления завершенного задания."""
        completed_shift = get_object_or_404(CompletedShiftAssignment, id=id)
        completed_shift.delete()

        return redirect('users:user_profile', pk=request.user.id)


class ShiftAssignmentDetailView(DetailView):
    """
    Представление для отображения деталей сменного задания.

    Это представление показывает информацию о конкретном задании.
    """

    model = ShiftAssignment
    template_name = 'shift_assignment/shift_assignment_detail.html'
    context_object_name = 'assignment'


class ShiftAssignmentUpdateView(UpdateView):
    """
    Представление для обновления сменного задания.

    Это представление обрабатывает обновление существующего задания.
    """

    model = ShiftAssignment
    form_class = ShiftAssignmentForm
    template_name = 'shift_assignment/shift_assignments_update.html'

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного обновления."""
        return reverse_lazy('users:user_profile', kwargs={'pk': self.request.user.pk})


class ShiftAssignmentDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление для удаления сменного задания.

    Это представление обрабатывает удаление существующего задания.
    """

    model = ShiftAssignment
    template_name = 'shift_assignment/shift_assignment_delete.html'

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного удаления."""
        return reverse_lazy('users:user_profile', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        """Получает объект по первичному ключу (pk)."""
        return get_object_or_404(ShiftAssignment, pk=self.kwargs['pk'])



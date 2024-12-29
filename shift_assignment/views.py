from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView

from .forms import ShiftAssignmentForm
from .models import ShiftAssignment
from users.models import UserRoles


import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import ShiftAssignment
from django.http import JsonResponse


class UploadShiftAssignmentView(LoginRequiredMixin, View):
    template_name = 'shift_assignment/upload_shift_assignment.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST' and 'file' in request.FILES:
            file = request.FILES['file']
            try:
                # Проверка формата файла
                if not file.name.endswith(('.xls', '.xlsx')):
                    return JsonResponse({'status': 'error', 'message': 'Неподдерживаемый формат файла.'})

                # Парсинг Excel файла
                df = pd.read_excel(file)

                # Проверка наличия необходимых столбцов
                required_columns = ['batch_number', 'operation_name', 'quantity', 'operator_id', 'part_id', 'machine_id']
                missing_columns = [col for col in required_columns if col not in df.columns]

                if missing_columns:
                    return JsonResponse({'status': 'error', 'message': f'Отсутствуют обязательные столбцы: {", ".join(missing_columns)}'})

                # Получаем модель пользователя
                User = get_user_model()

                # Логика для сохранения данных из DataFrame в базу данных
                for index, row in df.iterrows():
                    operator_id = row['operator_id']
                    try:
                        operator = User.objects.get(id=operator_id)  # Получите объект пользователя по ID
                    except User.DoesNotExist:
                        return JsonResponse({'status': 'error', 'message': f'Пользователь с ID {operator_id} не найден.'})

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


class ShiftAssignmentListView(ListView):
    model = ShiftAssignment
    template_name = 'shift_assignment/shift_assignment_list.html'
    context_object_name = 'assignments'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.role in [UserRoles.MASTER, UserRoles.ADMIN]:
            queryset = queryset.filter(master=self.request.user)
        elif self.request.user.role == UserRoles.OPERATOR:
            queryset = queryset.filter(operator=self.request.user)
        return queryset


class ShiftAssignmentDetailView(DetailView):
    model = ShiftAssignment
    template_name = 'shift_assignment/shift_assignment_detail.html'
    context_object_name = 'assignment'


class ShiftAssignmentUpdateView(UpdateView):
    model = ShiftAssignment
    form_class = ShiftAssignmentForm
    template_name = 'shift_assignment/shift_assignments_update.html'

    def get_success_url(self):
        # Перенаправляем на профиль текущего пользователя после успешного обновления
        return reverse_lazy('users:user_profile', kwargs={'pk': self.request.user.pk})


class ShiftAssignmentDeleteView(LoginRequiredMixin, DeleteView):
    model = ShiftAssignment
    template_name = 'shift_assignment/shift_assignment_delete.html'

    def get_success_url(self):
        # Возвращаем URL для перенаправления на профиль текущего пользователя
        return reverse_lazy('users:user_profile', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        return get_object_or_404(ShiftAssignment, pk=self.kwargs['pk'])


class OperatorAssignmentsView(View):
    def get(self, request):
        if request.user.role == UserRoles.OPERATOR:
            assignments = ShiftAssignment.objects.filter(operator=request.user)
        else:
            assignments = ShiftAssignment.objects.all()  # Или другой подход в зависимости от вашей логики
        return render(request, 'assignments.html', {'assignments': assignments})

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from shift_assignment.models import ShiftAssignment
from django.views import View
from django.http import JsonResponse
from .models import ProcessHistory
import json


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'process_history/home.html'


class CreateProcessHistoryView(View):
    def get(self, request, assignment_id):
        shift_assignment = get_object_or_404(ShiftAssignment, id=assignment_id)
        return render(request, 'create_process_history.html', {'assignment': shift_assignment})

# Шаблон create_process_history.html


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

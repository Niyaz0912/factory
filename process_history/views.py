from django.shortcuts import render, redirect
from .models import ProcessHistory  # Импортируйте вашу модель


def process_history_view(request, task_id):
    if request.method == 'POST':
        # Обработка данных формы
        for i in range(1, len(request.POST) // 4 + 1):
            control_code = request.POST.get(f'control_code_{i}')
            mark = request.POST.get(f'mark_{i}')
            quantity = request.POST.get(f'quantity_{i}')
            param_count = request.POST.get(f'param_count_{i}') == '+'

            # Сохранение данных в базе данных
            ProcessHistory.objects.create(
                task_id=task_id,
                control_code=control_code,
                mark=mark,
                quantity=quantity,
                param_count=param_count
            )

        return redirect('success_page')  # Перенаправление на страницу успеха или другую страницу

    # Получение параметров для отображения на странице
    parameters = get_parameters_for_task(task_id)  # Реализуйте эту функцию для получения параметров
    return render(request, 'process_history/process_history.html', {'parameters': parameters})
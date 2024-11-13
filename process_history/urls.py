from django.urls import path
from .views import (
    ShiftAssignmentView,
    HistoryProcessCreateView,
    CompleteProcessHistoryView,
    ShiftAssignmentsUpdateView,
    login_view,
    logout_view,  # Импортируем функцию выхода
    HomePageView,
)

app_name = 'process_history'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Главная страница
    path('login/', login_view, name='login'),  # Страница входа
    path('logout/', logout_view, name='logout'),  # Страница выхода
    path('shift_assignment/', ShiftAssignmentView.as_view(), name='shift_assignment'),  # Страница сменных заданий
    path('history_process_create/', HistoryProcessCreateView.as_view(), name='history_process_create'),  # Создание истории процесса
    path('complete_process_history/', CompleteProcessHistoryView.as_view(), name='complete_process_history'),  # Завершение истории процесса
    path('shift_assignments_update/', ShiftAssignmentsUpdateView.as_view(), name='shift_assignments_update'),  # Обновление сменных заданий
]

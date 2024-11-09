# from django.urls import path
# from . import views
# from process_history.views import ProcessHistoryListView, ProcessHistoryCreateView, \
#     ProcessHistoryDetailView, ProcessHistoryUpdateView
#
# app_name = 'process_history'  # Убедитесь, что вы используете пространство имен для приложения
#
# urlpatterns = [
#         path('', views.index, name='index'),
#         path('process_history/process_history_list/', ProcessHistoryListView.as_view(), name='process_histories'),
#         path('process_history/process_history/', ProcessHistoryCreateView.as_view(), name='process_history_create'),
#         path('process_history/process_history_detail/', ProcessHistoryDetailView.as_view(),
#              name='process_history_detail'),
#
# ]
#
# from django.urls import path
# from .views import (
#     ProcessHistoryListView,
#     ProcessHistoryCreateView,
#     ProcessHistoryDetailView,
#     ProcessHistoryUpdateView,
# )
#
# app_name = 'process_history'
#
# urlpatterns = [
#     path('', ProcessHistoryCreateView.as_view(), name='process history'),  # Главная страница
#     path('process_history_list/', ProcessHistoryListView.as_view(), name='process_histories'),  # Список историй процессов
#     path('process_history_create/', ProcessHistoryCreateView.as_view(), name='process_history_create'),  # Создание новой истории процесса
#     path('process_history_detail/', ProcessHistoryDetailView.as_view(), name='process_history_detail'),  # Подробная информация о процессе
#     path('<int:pk>/update/', ProcessHistoryUpdateView.as_view(), name='process_history_update'),  # Обновление истории процесса
# ]

from django.urls import path
from .views import (
    ShiftAssignmentView,
    HistoryProcessCreateView,
    CompleteProcessHistoryView,
    ShiftAssignmentsUpdateView,
    login_view,
)

app_name = 'process_history'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('shift_assignment/', ShiftAssignmentView.as_view(), name='shift_assignment'),
    path('history_process_create/', HistoryProcessCreateView.as_view(), name='history_process_create'),
    path('complete_process_history/', CompleteProcessHistoryView.as_view(), name='complete_process_history'),
    path('shift_assignments_update/', ShiftAssignmentsUpdateView.as_view(), name='shift_assignments_update'),
]

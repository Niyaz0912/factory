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

from django.urls import path
from .views import (
    HomePageView,
    ShiftAssignmentView,
    HistoryProcessCreateView,
    CompleteProcessHistoryView,
    ShiftAssignmentsUpdateView,
)

app_name = 'process_history'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shift_assignment/', ShiftAssignmentView.as_view(), name='shift_assignment'),
    path('history_process_create/<int:assignment_id>/', HistoryProcessCreateView.as_view(), name='history_process_create'),
    path('complete_process_history/', CompleteProcessHistoryView.as_view(), name='complete_process_history'),
    path('shift_assignments_update/<int:assignment_id>/', ShiftAssignmentsUpdateView.as_view(), name='shift_assignments_update'),
]

from django.urls import path
from .views import (
    HomePageView,
    ShiftAssignmentUpdateView,
    ShiftAssignmentDetailView,
    ShiftAssignmentCreateView,
    HistoryProcessCreateView,
    ShiftAssignmentListView
)

app_name = 'process_history'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shift_assignment_list/', ShiftAssignmentListView.as_view(), name='shift_assignment_list'),
    path('shift_assignment/<int:pk>/', ShiftAssignmentDetailView.as_view(), name='shift_assignment_detail'),  # Изменено
    path('history_process_create/<int:assignment_id>/', HistoryProcessCreateView.as_view(), name='history_process_create'),  # Добавлен assignment_id
    path('shift_assignments_update/<int:pk>/', ShiftAssignmentUpdateView.as_view(), name='shift_assignments_update'),  # Изменено на pk
    path('shift_assignment_create_update/', ShiftAssignmentCreateView.as_view(), name='shift_assignment_create'),
]
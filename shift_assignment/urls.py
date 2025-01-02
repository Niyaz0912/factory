from django.urls import path
from .views import (
    ShiftAssignmentListView,
    ShiftAssignmentUpdateView, OperatorAssignmentsView,
    ShiftAssignmentDeleteView, ShiftAssignmentDetailView, UploadShiftAssignmentView, CompletedShiftAssignmentListView
)

app_name = 'shift_assignment'

urlpatterns = [
    path('upload/', UploadShiftAssignmentView.as_view(), name='upload_shift_assignment'),  # Загрузка сменного задания
    path('shift_assignment/<int:pk>/delete/', ShiftAssignmentDeleteView.as_view(), name='delete_shift'),
    path('assignments/', OperatorAssignmentsView.as_view(), name='operator_assignments'),
    path('assignments/', ShiftAssignmentListView.as_view(), name='shift_assignment_list'),
    path('completed_assignments/', CompletedShiftAssignmentListView.as_view(), name='completed_shift_assignment_list'),
    path('detail/<int:pk>/', ShiftAssignmentDetailView.as_view(), name='shift_assignment_detail'),
    path('shift_assignment/<int:pk>/update/', ShiftAssignmentUpdateView.as_view(), name='update_shift'),
]

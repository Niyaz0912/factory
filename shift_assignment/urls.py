from django.urls import path
from .views import (
    ShiftAssignmentUpdateView, OperatorAssignmentsView,
    ShiftAssignmentDeleteView, ShiftAssignmentDetailView, UploadShiftAssignmentView, CompletedShiftAssignmentView
)

app_name = 'shift_assignment'

urlpatterns = [
    path('upload/', UploadShiftAssignmentView.as_view(), name='upload_shift_assignment'),  # Загрузка сменного задания
    path('shift_assignment/<int:pk>/delete/', ShiftAssignmentDeleteView.as_view(), name='delete_shift'),
    path('assignments/', OperatorAssignmentsView.as_view(), name='operator_assignments'),
    path('completed/<int:pk>/', CompletedShiftAssignmentView.as_view(), name='completed_shift_assignment'),
    path('detail/<int:pk>/', ShiftAssignmentDetailView.as_view(), name='shift_assignment_detail'),
    path('shift_assignment/<int:pk>/update/', ShiftAssignmentUpdateView.as_view(), name='update_shift'),
]

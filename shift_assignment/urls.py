from django.urls import path
from .views import (
    ShiftAssignmentListView,
    ShiftAssignmentUpdateView, OperatorAssignmentsView,
    ShiftAssignmentDeleteView, ShiftAssignmentDetailView, UploadShiftAssignmentView
)

app_name = 'shift_assignment'

urlpatterns = [
    path('upload/', UploadShiftAssignmentView.as_view(), name='upload_shift_assignment'),  # Загрузка сменного задания
    path('assignments/', OperatorAssignmentsView.as_view(), name='operator_assignments'),
    path('list', ShiftAssignmentListView.as_view(), name='list'),
    path('detail/<int:pk>/', ShiftAssignmentDetailView.as_view(), name='shift_assignment_detail'),
    path('update/<int:pk>/', ShiftAssignmentUpdateView.as_view(), name='update_shift'),
    path('delete/<int:pk>/', ShiftAssignmentDeleteView.as_view(), name='delete_shift'),
]

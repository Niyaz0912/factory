from django.urls import path
from .views import (
    ShiftAssignmentUpdateView,
    ShiftAssignmentDeleteView,
    ShiftAssignmentDetailView,
    UploadShiftAssignmentView,
    CompletedShiftAssignmentView,
    CompletedShiftAssignmentUpdateView, DeleteCompletedShiftView
)

app_name = 'shift_assignment'  # Убедитесь, что это указано

urlpatterns = [
    path('upload/', UploadShiftAssignmentView.as_view(), name='upload_shift_assignment'),
    path('shift_assignment/<int:pk>/delete/', ShiftAssignmentDeleteView.as_view(), name='delete_shift'),
    path('completed/<int:pk>/', CompletedShiftAssignmentView.as_view(), name='completed_shift_assignment'),
    path('detail/<int:pk>/', ShiftAssignmentDetailView.as_view(), name='shift_assignment_detail'),
    path('shift_assignment/<int:pk>/update/', ShiftAssignmentUpdateView.as_view(), name='update_shift'),
    path('completed_shift_assignment/<int:pk>/update/', CompletedShiftAssignmentUpdateView.as_view(),
         name='completed_shift_assignment_update'),  # Новый маршрут
    path('delete_completed_shift/<int:id>/', DeleteCompletedShiftView.as_view(), name='delete_completed_shift'),
]

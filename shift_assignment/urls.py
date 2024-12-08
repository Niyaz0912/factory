from django.urls import path
from .views import (
    ShiftAssignmentListView,
    ShiftAssignmentCreateView,
    ShiftAssignmentUpdateView,
    ShiftAssignmentDeleteView, ShiftAssignmentDetailView
)

app_name = 'shift_assignment'

urlpatterns = [
    path('list', ShiftAssignmentListView.as_view(), name='list'),
    path('detail/<int:pk>/', ShiftAssignmentDetailView.as_view(), name='shift_assignment_detail'),
    path('create/', ShiftAssignmentCreateView.as_view(), name='create_shift'),
    path('update/<int:pk>/', ShiftAssignmentUpdateView.as_view(), name='update_shift'),
    path('delete/<int:pk>/', ShiftAssignmentDeleteView.as_view(), name='delete_shift'),
]

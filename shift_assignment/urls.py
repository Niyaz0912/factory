from django.urls import path
from .views import (
    ShiftAssignmentListView,
    ShiftAssignmentCreateView,
    ShiftAssignmentUpdateView,
    ShiftAssignmentDeleteView, ShiftAssignmentDetailView,
)

app_name = 'shift_assignment'

urlpatterns = [
 path('', ShiftAssignmentListView.as_view(), name='shift_assignment_list'),
 path('create/', ShiftAssignmentCreateView.as_view(), name='assignments_create'),
 path('detail/<int:pk>/', ShiftAssignmentDetailView.as_view(), name='shift_assignment_detail'),
 path('update/<int:pk>/', ShiftAssignmentUpdateView.as_view(), name='shift_assignment_update'),
 path('delete/<int:pk>/', ShiftAssignmentDeleteView.as_view(), name='shift_assignment_delete'),
 ]

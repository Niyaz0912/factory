from django.urls import path
from .views import (
    ShiftAssignmentListView,
    ShiftAssignmentCreateView,
    ShiftAssignmentUpdateView,
    ShiftAssignmentDeleteView, ShiftAssignmentDetailView
)

app_name = 'shift_assignment'

urlpatterns = [
    path('', ShiftAssignmentListView.as_view(), name='shift_assignment_list'),
    path('create/', ShiftAssignmentCreateView.as_view(), name='assignments_create'),
    path('<int:pk>/', ShiftAssignmentDetailView.as_view(), name='shift_assignment_detail'),
    path('<int:pk>/update/', ShiftAssignmentUpdateView.as_view(), name='assignments_update'),
    path('<int:pk>/delete/', ShiftAssignmentDeleteView.as_view(), name='assignments_delete'),
]

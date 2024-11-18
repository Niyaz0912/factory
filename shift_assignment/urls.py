from django.urls import path
from .views import (ShiftAssignmentListView, ShiftAssignmentCreateView, ShiftAssignmentDetailView,
                    ShiftAssignmentUpdateView, ShiftAssignmentDeleteView
                    )

app_name = 'shift_assignment'

urlpatterns = [
    path('', ShiftAssignmentListView.as_view(), name='assignments_list'),
    path('create/', ShiftAssignmentCreateView.as_view(), name='shift_assignment_create'),
    path('detail/', ShiftAssignmentDetailView.as_view(), name='shift_assignments_detail'),
    path('update/<int:pk>/', ShiftAssignmentUpdateView.as_view(), name='assignments_update'),
    path('delete<int:pk>/', ShiftAssignmentDeleteView.as_view(), name='assignments_delete'),
]

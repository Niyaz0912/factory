from django.urls import path
from .views import (
    HomePageView, ShiftAssignmentUpdateView, ShiftAssignmentDetailView, ShiftAssignmentCreateView,
    HistoryProcessCreateView

)

app_name = 'process_history'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shift_assignment/', ShiftAssignmentDetailView.as_view(), name='shift_assignment'),
    path('history_process_create/<int:assignment_id>/', HistoryProcessCreateView.as_view(),
         name='history_process_create'),
    path('shift_assignments_update/<int:assignment_id>/', ShiftAssignmentUpdateView.as_view(),
         name='shift_assignments_update'),
    path('shift_assignment/create/', ShiftAssignmentCreateView.as_view(), name='shift_assignment_create'),
]

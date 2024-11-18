from django.urls import path
from .views import (
    HomePageView, HistoryProcessCreateView,
)

app_name = 'process_history'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('history_process_create/<int:assignment_id>/', HistoryProcessCreateView.as_view(), name='history_process_create'),
]

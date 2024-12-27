from django.urls import path
from .views import HomePageView, SaveProcessHistoryView, HistoryProcessCreateView

app_name = 'process_history'

urlpatterns = [
    path('history/create/<int:assignment_id>/', HistoryProcessCreateView.as_view(), name='history_process_create'),

    path('', HomePageView.as_view(), name='home'),
    path('save-process-history/', SaveProcessHistoryView.as_view(), name='save_process_history'),
]
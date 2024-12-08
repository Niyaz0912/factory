from django.urls import path
from .views import HistoryProcessCreateView, save_process_history, HomePageView

app_name = 'process_history'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('process/history/create/<int:assignment_id>/', HistoryProcessCreateView.as_view(), name='history_process_create'),
    path('process/history/save/', save_process_history, name='save_process_history'),
]

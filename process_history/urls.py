from django.urls import path
from .views import HomePageView, SaveProcessHistoryView, CreateProcessHistoryView

app_name = 'process_history'

urlpatterns = [
    path('create-process-history/<int:assignment_id>/', CreateProcessHistoryView.as_view(), name='create_process_history'),
    path('', HomePageView.as_view(), name='home'),
    path('save-process-history/', SaveProcessHistoryView.as_view(), name='save_process_history'),
]
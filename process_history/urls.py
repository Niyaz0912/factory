from django.urls import path
from .views import HomePageView, SaveProcessHistoryView, HistoryProcessCreateView

app_name = 'process_history'

urlpatterns = [
    path('create/<int:pk>/', HistoryProcessCreateView.as_view(), name='history_process_create'),
    path('', HomePageView.as_view(), name='home'),
    path('save_process_history/<int:assignment_id>/', SaveProcessHistoryView.as_view(), name='save_process_history'),
]
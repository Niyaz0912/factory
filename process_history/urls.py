from django.urls import path
from .views import HomePageView, SaveProcessHistoryView, HistoryProcessCreateView

# Указываем пространство имен для приложения process_history
app_name = 'process_history'

urlpatterns = [
    # URL для создания новой записи истории процесса по первичному ключу (pk)
    path('create/<int:pk>/', HistoryProcessCreateView.as_view(), name='history_process_create'),

    # URL для главной страницы приложения
    path('', HomePageView.as_view(), name='home'),

    # URL для сохранения истории процесса, связанного с заданием (assignment_id)
    path('save_process_history/<int:assignment_id>/', SaveProcessHistoryView.as_view(), name='save_process_history'),
]

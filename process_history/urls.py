from django.urls import path
from .views import process_history_view

urlpatterns = [
    path('process_history/<int:task_id>/', process_history_view, name='process_history'),
]
from django.urls import path
from .views import (
    ShiftAssignmentUpdateView,
    ShiftAssignmentDeleteView,
    ShiftAssignmentDetailView,
    UploadShiftAssignmentView,
    CompletedShiftAssignmentView,
    CompletedShiftAssignmentUpdateView,
    DeleteCompletedShiftView
)

# Указываем пространство имен для приложения shift_assignment
app_name = 'shift_assignment'  # Убедитесь, что это указано

urlpatterns = [
    # URL для загрузки нового задания
    path('upload/', UploadShiftAssignmentView.as_view(), name='upload_shift_assignment'),

    # URL для удаления задания по его первичному ключу (pk)
    path('shift_assignment/<int:pk>/delete/', ShiftAssignmentDeleteView.as_view(), name='delete_shift'),

    # URL для просмотра завершенного задания по его первичному ключу (pk)
    path('completed/<int:pk>/', CompletedShiftAssignmentView.as_view(), name='completed_shift_assignment'),

    # URL для просмотра деталей задания по его первичному ключу (pk)
    path('detail/<int:pk>/', ShiftAssignmentDetailView.as_view(), name='shift_assignment_detail'),

    # URL для обновления задания по его первичному ключу (pk)
    path('shift_assignment/<int:pk>/update/', ShiftAssignmentUpdateView.as_view(), name='update_shift'),

    # URL для обновления завершенного задания по его первичному ключу (pk)
    path('completed_shift_assignment/<int:pk>/update/', CompletedShiftAssignmentUpdateView.as_view(),
         name='completed_shift_assignment_update'),  # Новый маршрут

    # URL для удаления завершенного задания по его идентификатору (id)
    path('delete_completed_shift/<int:id>/', DeleteCompletedShiftView.as_view(), name='delete_completed_shift'),
]

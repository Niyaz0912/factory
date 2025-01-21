from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from process_history.views import HomePageView

# Определение маршрутов (URL) для проекта
urlpatterns = [
    # URL для административной панели
    path('admin/', admin.site.urls),

    # Главная страница, обрабатываемая представлением HomePageView
    path('', HomePageView.as_view(), name='home'),

    # Подключение маршрутов приложения пользователей
    path('users/', include('users.urls', namespace='users')),

    # Подключение маршрутов приложения истории процессов
    path('process_history/', include('process_history.urls', namespace='process_history')),

    # Подключение маршрутов приложения назначения смен
    path('shift_assignment/', include('shift_assignment.urls', namespace='shift_assignment')),
]

# Если проект находится в режиме отладки (DEBUG), добавляем обработку статических файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


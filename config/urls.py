from django.contrib import admin
from django.urls import path, include
from process_history.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),  # Добавлен маршрут для корневого URL
    path('users/', include('users.urls', namespace='users')),
    path('', include('process_history.urls')),  # Подключение маршрутов приложения process_history
]
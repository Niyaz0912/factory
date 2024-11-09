# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import RedirectView
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('process_history/', include('process_history.urls')),
#     path('', RedirectView.as_view(url='process_history/')),  # Перенаправление на process_history
# ]

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('process_history', include('process_history.urls')),  # Импортируйте маршруты приложения process_history
#     path('', RedirectView.as_view(url='process_history/')),  # Перенаправление на process_history
# ]


# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('process_history/', include('process_history.urls')),  # Подключение маршрутов вашего приложения
# ]

from django.contrib import admin
from django.urls import path, include
from process_history.views import HomePageView  # Импортируйте новое представление

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),  # Добавлен маршрут для корневого URL
    path('accounts/', include('django.contrib.auth.urls')),  # Стандартные URL для аутентификации
    path('', include('process_history.urls')),  # Подключение маршрутов приложения process_history
]
from django.contrib import admin
from django.urls import path, include
from process_history.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('users/', include('users.urls', namespace='users')),
    path('process_history/', include('process_history.urls', namespace='process_history')),
    path('shift_assignment/', include('shift_assignment.urls', namespace='shift_assignment')),
    ]

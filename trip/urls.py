from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, trip_list

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', trip_list, name='trip_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

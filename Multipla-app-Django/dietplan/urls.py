
from django.contrib import admin
from django.urls import path, include
from dietapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
         path('', include('dietapp.urls', namespace='dietapp')),
          path('account/', include('accounts.urls', namespace='accounts')), 
          path('profile', include('profile.urls', namespace='profile')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

app_name = 'dietapp'

urlpatterns = [
    path('', views.index, name='homepage'),
path('health_post/', views.health_post, name='health_post'),
path('health_data/', views.health_data, name='health_data'),
]

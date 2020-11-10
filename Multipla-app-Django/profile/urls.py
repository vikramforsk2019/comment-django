from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.profile, name='profile'),
path('/edit/', views.edit, name='edit'),
path('/edit_data/', views.edit_data, name='edit_data'),
]

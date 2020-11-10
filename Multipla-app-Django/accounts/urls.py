from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
     path('signup_insert/', views.signup_insert, name='signup_insert'),
     path('logout/', views.logout, name='logout'),#namespace    account:logout
     path('account_delete/', views.account_delete, name='account_delete'),
]

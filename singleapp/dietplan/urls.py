
from django.contrib import admin
from django.urls import path
from dietapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
      path('signup/', views.signup),
       path('signin/', views.signin),
       path('', views.index),    
          path('profile/', views.profile),

            path('signup_insert/', views.signup_insert),
              path('login/', views.login),
                path('logout/', views.logout),
                   path('health_post/', views.health_post),
                    path('health_data/', views.health_data),
         path('edit/', views.edit),
         path('edit_data/', views.edit_data),
          path('account_delete/', views.account_delete),
]

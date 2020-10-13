"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from products import views

urlpatterns = [
    path('', views.index, name='index'),
    #Ajax requests
    path('products/', views.get, name='get_products'),
    path('productupdated/', views.update_product, name='update_products'),
    path('productadded/', views.post_product, name='post_product'),
    path('productremoved/', views.delete_product, name='delete_product'),
path('commentadd/', views.commentadd, name='commentadd'),
path('comment/', views.comment, name='comment'),
    path('admin/', admin.site.urls),
]
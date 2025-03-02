"""
URL configuration for nqviet_project01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from book.views import book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),  # URL của ứng dụng cart
    path('', book_list, name='home'),  # Trang chủ là danh sách sách
    path('', include('book.urls', namespace='book')),  # URL của ứng dụng book
    path('accounts/', include('django.contrib.auth.urls')),  # URL mặc định cho login/logout
    path('users/', include('customer.urls')),
    # path('api/', include('apis.urls')),  # URL của ứng dụng apis
]

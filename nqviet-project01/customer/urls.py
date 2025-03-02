from django.urls import path
from .views import customer_list

app_name = 'customer'

urlpatterns = [
    path('', customer_list, name='user_list'),
]

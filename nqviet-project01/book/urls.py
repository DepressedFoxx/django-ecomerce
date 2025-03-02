from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('new/', views.book_create, name='book_create'),
    path('<int:pk>/edit/', views.book_update, name='book_update'),
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/login/', views.login_view, name='login'),
    path("signup/", views.signup_view, name="signup"),
]

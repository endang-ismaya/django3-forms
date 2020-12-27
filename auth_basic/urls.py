from django.urls import path
from auth_basic.views import index, user_login, user_registration, user_logout, user_dashboard

app_name = 'auth_basic'

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', user_registration, name='user_register'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
]

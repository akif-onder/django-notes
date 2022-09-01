from multiprocessing.util import is_abstract_socket_namespace
from django.urls import path
from .views import register, user_login, user_logout

urlpatterns = [
    path('logout/', user_logout, name='user_logout'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
]
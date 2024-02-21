from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout'),
    
]
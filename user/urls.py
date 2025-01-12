from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from user.views import *

urlpatterns = [
    path('register/', register, name = 'register'),
    path('login/', login_view, name = 'user_login'),
    path('logout/', logout_view, name = 'logout'),
    path('profile/', profile, name='user_profile'),
    path('profile_update/', profile_update, name = 'user_profile_update'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),

  ]
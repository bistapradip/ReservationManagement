from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home, name = 'home'),
    path('staff/', Staff, name = 'staff'),
    path('Enquiry/', enquiry, name = 'Enquiry'),
    path('Confirmed/', confirmed, name = 'Confirmed'),
    path('foc/', foc, name = "FOC"),
    path('Confirmed/delete/<int:pk>', confirmed_delete, name = "Confirmed_delete"),
    path('Confirmed/update/<int:pk>', confirmed_edit, name = "Confirmed_edit"),
    path('staff/profile/view/<int:pk>', Staff_detail, name = "Staff_detail"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


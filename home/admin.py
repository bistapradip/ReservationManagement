from django.contrib import admin
from .models import *
from django.utils.html import format_html

class ConfirmedAdmin(admin.ModelAdmin):
    ordering = ['date']
    list_display = ['date','sector', 'agency']

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['date','sector', 'agency']

class staffAdmin(admin.ModelAdmin):
    list_display = ['image_tag','name', 'email']

class FOCAdmin(admin.ModelAdmin):
    list_display = ['date', 'sector', 'name']




admin.site.site_header = "Admin Debonair"
# Register your models here.
admin.site.register(staff,staffAdmin)
admin.site.register(Enquiry,EnquiryAdmin)
admin.site.register(Confirmed,ConfirmedAdmin)
admin.site.register(FOC, FOCAdmin)
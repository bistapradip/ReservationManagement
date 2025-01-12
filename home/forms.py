from django import forms
from .models import Confirmed, FOC, Enquiry

class ConfirmedForm(forms.ModelForm):
    class Meta:
        model = Confirmed
        fields = ['date', 'sector', 'paxNo', 'airline', 'agency', 'reference', 'remarks', 'flightno']

class FOCForm(forms.ModelForm):
    class Meta:
        model = FOC
        fields = "__all__"

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        
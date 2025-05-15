from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'inquiry_type', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'cmd-input'}),
            'email': forms.EmailInput(attrs={'class': 'cmd-input'}),
            'inquiry_type': forms.Select(attrs={'class': 'cmd-input'}),
            'subject': forms.TextInput(attrs={'class': 'cmd-input'}),
            'message': forms.Textarea(attrs={'class': 'cmd-input', 'rows': 5}),
        }

from django import forms
from .models import Tip

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['subject', 'description','image']

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the description here'}),
        }

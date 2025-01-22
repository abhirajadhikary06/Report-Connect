from django import forms
from .models import HarassmentReport

class HarassmentReportForm(forms.ModelForm):
    class Meta:
        model = HarassmentReport
        fields = ['location', 'time', 'date', 'harassment_type', 'description']
        widgets = {
            'time': forms.TimeInput(attrs={'placeholder': 'e.g., 10:30:00'}),
            'date': forms.DateInput(attrs={'placeholder': 'e.g., 2025-01-01'}),
        }

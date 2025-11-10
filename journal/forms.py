from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Start typing your thoughts here...',
                'rows': 5,
                'style': 'width: 100%; border-radius: 8px; border: 1px solid #d6336c; padding: 12px; font-size: 1rem; font-family: inherit; color: #611a3b;',
            })
        }

from django import forms
from .models import Pdfs


class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdfs
        fields = ('university', 'branch', 'subject', 'pdf')

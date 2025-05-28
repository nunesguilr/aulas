from django import forms
from .models import Setor


class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['nome', 'filiais']

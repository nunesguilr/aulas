from .models import Pessoa
from django.forms import ModelForm

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade', 'cidade', 'estado']

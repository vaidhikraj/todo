from django.forms import ModelForm
from .models import Ntodo

class Ntodoform(ModelForm):
    class Meta:
        model=Ntodo
        fields=['title','desc','important']
        
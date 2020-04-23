from django import forms

from .models import  Symx

class nSymx(forms.ModelForm):

    class Meta:
        model = Symx
        fields = '__all__'

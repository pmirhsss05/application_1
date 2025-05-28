from django import forms
from django.forms import ModelForm
from .models import Model_X


class Form_x(forms.Form):
    widget=forms.TextInput(attrs={'class': 'form-control'})
    task = forms.CharField(initial = "Дано вещественное число. Определить, какое это число: положительное, отрицательное, ноль.")
    x = forms.IntegerField(initial=3)


class Model_form_X(ModelForm):

    class Meta:
        model = Model_X
        fields = '__all__'
        print('\nfields: ', fields)

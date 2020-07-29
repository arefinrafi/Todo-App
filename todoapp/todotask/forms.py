from django import forms
from django.forms import ModelForm
from .models import Task


class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the new Task....'}))

    class Meta:
        model = Task
        fields = '__all__'

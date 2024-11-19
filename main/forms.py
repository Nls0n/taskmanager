from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Придумай уже что-нибудь, а'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Шо будем делать то'
            }),
        }
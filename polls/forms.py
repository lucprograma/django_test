from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    form for creating or modify a task
    """
    class Meta:
        """
        Inner class for the form with all the properties    
        """
        model = Task
        fields = ['title', 'description', 'state']
        exclude = ['user_ref']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description', 'rows': 3}),
            'state': forms.Select(attrs={'class': 'form-control'}),
        }

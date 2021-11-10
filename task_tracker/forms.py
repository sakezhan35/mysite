from django import forms
from .models import Task


# Форма задачи
class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'title', 'description', 'performer',
            'observers', 'start_date', 'start_time',
            'end_date', 'end_time', 'status',
            'planned_end_date', 'planned_end_time',
        ]

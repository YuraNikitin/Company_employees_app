import datetime
from django import forms
from ..model.worker import Worker


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'surname', 'lastName', 'dateBirth', 'email', 'phone', 'endDate', 'position', 'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.Textarea(attrs={'class': 'form-control'}),
            'dateBirth': forms.SelectDateWidget(years = range(datetime.datetime.today().year, 1950,-1)),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'endDate': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(),
        }

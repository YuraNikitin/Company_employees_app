from django import forms
from django.core.exceptions import ValidationError
from ..model.department import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Department.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError("Slug must be unique. We have '{}' slug already".format(new_slug))
        return new_slug

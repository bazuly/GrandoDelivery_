from django import forms
from .models import UploadDriverData


class DriverForm(forms.ModelForm):
    class Meta:
        model = UploadDriverData
        fields = ['name', 'org_name', 'other_data', 'files']


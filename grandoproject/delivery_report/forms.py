from .models import DeliveryReport, EmailReportToClientSuccess
from django import forms
from manager_client.models import Client


class DeliveryReportForm(forms.ModelForm):
    class Meta:
        model = DeliveryReport
        fields = ['direction', 'driver_name', 'commentary', 'client_list', 'dispatcher']

        widgets = {
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'commentary': forms.Textarea(attrs={'class': 'form-control'}),
            'client_list': forms.Select(attrs={'class': 'form-control'}),
            'dispatcher': forms.Select(attrs={'class': 'form-control'}),
        }


class EmailReportToClientForm(forms.ModelForm):
    clients = forms.ModelChoiceField

    class Meta:
        model = EmailReportToClientSuccess
        fields = ['clients', 'direction', 'message', 'date']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),

        }

        def __init__(self, *args, **kwargs):
            super(EmailReportToClientForm, self).__init__(*args, **kwargs)
            self.fields['clients'].queryset = Client.objects.all()

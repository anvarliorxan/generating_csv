from django import forms
from .models import CSVData


class CSVDataForm(forms.ModelForm):
    class Meta:
        model = CSVData
        fields = ['full_name', 'job', 'email', 'domain_name', 'phone_number',
                  'company_name', 'text', 'integer', 'address', 'date']

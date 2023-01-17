from django import forms
from django.forms import formset_factory

from webapp.models import TestSampleReport


class AuthorForm(forms.Form):
    first_name = forms.CharField(label="Imię")
    last_name = forms.CharField(label="Nazwisko")


AuthorFormSet = formset_factory(AuthorForm, extra=1, min_num=1, max_num=2, validate_min=True)


class TestSampleReportForm(forms.ModelForm):
    class Meta:
        model = TestSampleReport
        exclude = ('author',)

        labels = {
            'supplier_name': "Nazwa dostawcy",
            'supplier_address': "Adres dostawcy",
            'receiver_name': "Nazwa odbiorcy",
            'receiver_address': "Adres odbiorcy",
            'mechanism_name': "Nazwa i symbol mechanizmu",
            'contract_id': "Numer zlecenia",
            'transport_method': "Sposób dostarczenia próbki"
        }

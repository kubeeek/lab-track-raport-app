import django.forms as forms
from django.forms import ModelForm

from webapp.models import TestSample
from bootstrap_datepicker_plus.widgets import DatePickerInput


class TestSampleForm(ModelForm):
    class Meta:
        model = TestSample
        fields = '__all__'

        labels = {
            'sample_code': "Kod próbki",
            'source_facility': "Placówka źródłowa",
            'description': "Asortyment",
            'admission_date': "Data przyjęcia",
            'expiration_date': "Data przydatności",
            'expiration_date_optional': "Komentarz dla daty (opcjonalnie)",
            'test_end_date': "Data zakończenia badań",
            'sample_size': "Rozmiar próbki",
            'appeal_test': "Analiza odwoławcza",
            'control_type': "Rodzaj kontroli",
            'customer_name': "Nazwa klienta",
            'type': "Rodzaj próbki",
            'sample_condition': "Stan próbki",
            'sample_method': "Metoda pobrania próbki"
        }

        widgets = {
            'sample_code': forms.TextInput(attrs={'placeholder': 'ABC321'}),
            'expiration_date_optional': forms.Textarea(attrs={
                'placeholder': "Spożyć w ciągu 5 godzin od otwarcia",
                'rows': 5,
            }),
            'description': forms.Textarea(attrs={'placeholder': 'Tekst', 'rows': 5}),
            'admission_date': DatePickerInput(),
            'expiration_date': DatePickerInput(),
            'test_end_date': DatePickerInput()
        }

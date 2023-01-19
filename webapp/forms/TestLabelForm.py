from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.forms import ModelForm

from webapp.models import TestLabel
import django.forms as forms

class TestLabelForm(ModelForm):

    class Meta:
        model = TestLabel
        fields = '__all__'


        labels = {
            'test_sample': "Próbka",
            'is_done': "Badanie wykonane",
            'parameter_name': 'Nazwa parametru',
            'value': "Wartość (odżywcza)",
            'labeling': 'Oznakowanie',
            'specification': 'Specyfikacja',
            'regulation': 'Rozporządzenie',
            'sample_amount': "Liczba próbek do badania",
            'test_result': "Wynik badania",
            'start_date': "Data rozpoczęcia",
            'end_date': "Data zakończenia",
            'method_status': "Status metody",
            'margin': 'Niepewność'
        }

        widgets = {
            'start_date': DatePickerInput(),
            'end_date': DatePickerInput(),
        }


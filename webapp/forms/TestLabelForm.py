from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from webapp.models import TestLabel


class TestLabelForm(ModelForm):
    def clean(self):
        regulation = self.cleaned_data.get('regulation')
        specification = self.cleaned_data.get('specification')
        labeling = self.cleaned_data.get('labeling')

        error_msg = "Conajmniej jedno z pól (specyfikacja, rozporządzenie, oznakowanie) musi zostać uzupełnione."

        if not regulation and not specification and not labeling:
            raise ValidationError(
                {
                    "regulation": error_msg,
                    "specification": error_msg,
                    "labeling": error_msg,
                },
            )

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
            'uncertainty': 'Niepewność',
            'type': 'Rodzaj badania'
        }

        widgets = {
            'start_date': DatePickerInput(),
            'end_date': DatePickerInput(),
        }

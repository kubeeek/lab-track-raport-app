from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms


class ExportForm(forms.Form):
    from_date = forms.DateTimeField(label='Od', required=False)
    to_date = forms.DateTimeField(label='Do', required=False)
    file_type = forms.TypedChoiceField(choices=[
        ('CSV', 'CSV'),
        ('XLSX', 'XLSX')
    ], label="Rodzaj pliku")

    from_date.widget = DatePickerInput()
    to_date.widget = DatePickerInput()

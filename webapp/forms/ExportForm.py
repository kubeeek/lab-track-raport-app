from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms

class ExportForm(forms.Form):
    from_date = forms.DateTimeField(label='Od', required=False)
    to_date = forms.DateTimeField(label='Do', required=False)

    from_date.widget = DatePickerInput()
    to_date.widget = DatePickerInput()

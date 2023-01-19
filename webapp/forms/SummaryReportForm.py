from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms


class SummaryReportForm(forms.Form):
    from_date = forms.DateField(label='Od', required=False)
    to_date = forms.DateField(label='Do', required=False)

    from_date.widget = DatePickerInput()
    to_date.widget = DatePickerInput(range_from="from_date")

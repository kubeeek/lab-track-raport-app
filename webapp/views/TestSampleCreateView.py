from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.views.generic import CreateView

from webapp.models import TestSample


class TestSampleCreateView(CreateView):
    fields = '__all__'
    model = TestSample


    def get_form(self):
        form = super().get_form()

        for key in form.fields.keys():
            if 'date' in key and 'optional' not in key:
                form.fields[key].widget = DatePickerInput()

        form.fields["description"].widget.attrs['rows'] = 5
        form.fields['expiration_date_optional'].widget.attrs['rows'] = 5
        return form

    def get_context_data(self, **kwargs):
        context = super(TestSampleCreateView, self).get_context_data(**kwargs)

        # if self.request.POST:
        #     context['test_sample_formset'] = TestSampleFormset(self.request.POST)
        # else:
        #     context['test_sample_formset'] = TestSampleFormset()

        return context

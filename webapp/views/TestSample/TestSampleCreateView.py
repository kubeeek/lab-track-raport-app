import datetime

from django.views.generic import CreateView

from webapp.forms import TestSampleForm
from webapp.models import TestSample
from webapp.views.common import OperationSuccessMessageViewMixin


class TestSampleCreateView(OperationSuccessMessageViewMixin, CreateView):
    model = TestSample
    form_class = TestSampleForm

    def get_initial(self):
        initial = super().get_initial()

        initial['admission_date'] = datetime.date.today()

        return initial

    def get_context_data(self, **kwargs):
        context = super(TestSampleCreateView, self).get_context_data(**kwargs)

        return context

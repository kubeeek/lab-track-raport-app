from django.views.generic.edit import UpdateView

from webapp.forms import TestSampleForm
from webapp.models import TestSample
from webapp.views.common import OperationSuccessMessageViewMixin


class TestSampleUpdateView(OperationSuccessMessageViewMixin, UpdateView):
    model = TestSample
    form_class = TestSampleForm

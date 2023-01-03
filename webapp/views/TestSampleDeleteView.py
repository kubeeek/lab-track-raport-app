from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from webapp.models import TestSample
from webapp.views.common import OperationSuccessMessageViewMixin


class TestSampleDeleteView(OperationSuccessMessageViewMixin, DeleteView):
    model = TestSample
    success_url = reverse_lazy('testsample_list')

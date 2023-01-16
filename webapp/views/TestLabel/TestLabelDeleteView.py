from django.urls import reverse
from django.views.generic.edit import DeleteView

from webapp.models import TestLabel
from webapp.views.common import OperationSuccessMessageViewMixin


class TestLabelDeleteView(OperationSuccessMessageViewMixin, DeleteView):
    model = TestLabel

    def get_success_url(self):
        return reverse('testsample_detail', kwargs={'pk': self.object.test_sample_id})

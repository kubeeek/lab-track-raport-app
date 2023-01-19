from django.views.generic.edit import UpdateView

from webapp.forms import TestLabelForm
from webapp.models import TestLabel
from webapp.views.common import OperationSuccessMessageViewMixin


class TestLabelUpdateView(OperationSuccessMessageViewMixin, UpdateView):
    model = TestLabel
    form_class = TestLabelForm

from django.views.generic.edit import UpdateView

from webapp.models import TestLabel
from webapp.forms import TestSampleUpdateForm

class TestLabelUpdateView(UpdateView):
    model = TestLabel

    fields = ['done', 'parameter_name']
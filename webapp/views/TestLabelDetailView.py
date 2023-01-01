from django.views.generic.detail import DetailView

from webapp.models import TestLabel


class TestLabelDetailView(DetailView):
    model = TestLabel

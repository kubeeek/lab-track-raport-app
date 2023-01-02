from django.views.generic.list import ListView

from webapp.models import TestSample


class TestSampleListView(ListView):
    model = TestSample
    paginate_by = 3

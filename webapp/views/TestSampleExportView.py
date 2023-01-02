from webapp.models import TestSample
from webapp.views.common import ExportView


class TestSampleExportView(ExportView):
    model = TestSample
    filename = 'testsample'
    fields = [f.name for f in model._meta.get_fields()][1:]
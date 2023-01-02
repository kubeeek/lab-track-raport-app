from webapp.models import TestSample
from webapp.views.common import ExportView


class TestSampleExportView(ExportView):
    model = TestSample
    filename = 'testsample'
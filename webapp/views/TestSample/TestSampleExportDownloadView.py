from webapp.models import TestSample
from webapp.utils.decorators import parse_timestamp_range
from webapp.views.common import ExportDownloadView


class TestSampleExportDownloadView(ExportDownloadView):
    model = TestSample
    filename = 'test_sample'
    fields = [f.name for f in model._meta.get_fields()][2:]

    @parse_timestamp_range()
    def get(self, request, filter_params, *args, **kwargs):
        return super().get(request, filter_params)

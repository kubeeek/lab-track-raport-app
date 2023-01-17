from webapp.models import TestLabel
from webapp.utils.decorators import parse_timestamp_range
from webapp.views.common import ExportDownloadView


class TestLabelExportDownloadView(ExportDownloadView):
    model = TestLabel
    filename = 'test_label'
    fields = [f.name for f in model._meta.get_fields()][1:]

    @parse_timestamp_range()
    def get(self, request, filter_params, *args, **kwargs):
        return super().get(request, filter_params)

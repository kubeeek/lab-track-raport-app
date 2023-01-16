from webapp.models import TestSample
from webapp.utils.decorators import parse_timestamp_range
from webapp.views.common import ExportView


class TestSampleExportView(ExportView):
    model = TestSample
    filename = 'test_sample'
    fields = [f.name for f in model._meta.get_fields()][1:]

    @parse_timestamp_range(TestSample)
    def get(self, request, from_date, to_date, *args, **kwargs):
        return super().get(request, {"from_date": from_date, "to_date": to_date})

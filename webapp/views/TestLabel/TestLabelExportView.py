from webapp.models import TestLabel
from webapp.utils.decorators import parse_timestamp_range
from webapp.views.common import ExportView


class TestLabelExportView(ExportView):
    model = TestLabel
    filename = 'test_label'
    fields = [f.name for f in model._meta.get_fields()][1:]

    @parse_timestamp_range(TestLabel)
    def get(self, request, from_date, to_date, *args, **kwargs):
        return super().get(request, {"from_date": from_date, "to_date": to_date})

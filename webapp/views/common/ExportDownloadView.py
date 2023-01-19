from django.db import transaction
from django.views import View

from webapp.models.common import ModelWithTimestamp
from webapp.utils.writers import CSVStreamingResponse, XLSXStreamingResponse


class ExportDownloadView(View):
    fields = []
    model = ModelWithTimestamp
    filename = None

    def get(self, request, filter_params=None):
        file_type = request.GET.get('file_type', 'csv').lower()

        with transaction.atomic():
            streaming_response = None

            if filter_params is None:
                queryset = self.model.objects
            else:
                queryset = self.model.objects.filter(
                    created_at__range=[filter_params['from_date'], filter_params['to_date']]
                )

            if file_type == 'csv':
                streaming_response = CSVStreamingResponse(self.fields, self.filename, queryset)
            elif file_type == 'xlsx':
                streaming_response = XLSXStreamingResponse(self.fields, self.filename, queryset)

            return streaming_response.get()


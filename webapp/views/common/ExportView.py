from django.db import models
from django.db import transaction
from django.views import View

from webapp.models.common import ModelWithTimestamp
from webapp.utils.writers import CSVStream, CSVIterableWrapper

class ExportView(View):
    fields = []
    model = ModelWithTimestamp
    filename = None

    def get(self, request, filter_params=None):

        with transaction.atomic():
            if filter_params is None:
                queryset = self.model.objects
            else:
                queryset = self.model.objects.filter(
                    created_at__range=[filter_params['from_date'], filter_params['to_date']]
                )

            iterator = queryset.iterator()

            counter = CSVIterableWrapper(self.fields, iterator)
            csv_stream = CSVStream()

            return csv_stream.export(self.filename, counter)

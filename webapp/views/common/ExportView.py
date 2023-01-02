from django.db import transaction
from django.views import View

from webapp.models import TestSample
from webapp.utils.writers import CSVStream, CSVIterableWrapper


class ExportView(View):
    def get(self, request, *args, **kwargs):
        fields = [f.name for f in TestSample._meta.get_fields()]

        with transaction.atomic():
            iterator = self.model.objects.iterator()

            counter = CSVIterableWrapper(fields, iterator)
            csv_stream = CSVStream()

            return csv_stream.export(self.filename, counter)

import csv
import io
import os

import xlsx_streaming
from django.http import StreamingHttpResponse
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

from jibadproject import settings
from webapp.models import TestSample


class XLSXStreamingResponse:
    def __init__(self, fields, filename, queryset):
        self.fields = fields
        self.path_string = os.path.join(settings.BASE_DIR, 'webapp/templates/webapp/template.xlsx')
        self.qs = queryset.values_list()
        self.filename = filename

    def get(self):
        wb = Workbook()
        ws = wb.active

        ws.append(['id'] + self.fields)
        ws.append(['id'] + self.fields)

        memory_file = io.BytesIO(save_virtual_workbook(wb))

        stream = xlsx_streaming.stream_queryset_as_xlsx(
            self.qs,
            memory_file,
            batch_size=50
        )

        response = StreamingHttpResponse(
            stream,
            content_type='application/vnd.xlsxformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = f'attachment; filename={self.filename}.xlsx'

        return response


class CSVStreamingResponse:
    def __init__(self, fields, filename, queryset):
        self.fields = fields
        self.filename = filename
        self.qs = queryset

    def get(self):
        data = CSVIterableWrapper(self.fields, self.qs.iterator())
        return CSVStream().export(self.filename, data)


class CSVIterableWrapper:
    def __init__(self, fields_list, model_iterator):
        self.returnedFields = False
        self.fields = fields_list
        self.iterator = model_iterator

    def __iter__(self):
        return self

    def __next__(self):
        if self.returnedFields:
            next_model_instance = next(self.iterator)
            return next_model_instance.serialize()

        self.returnedFields = True

        # byte to mark it is utf8 encoded csv file
        self.fields[0] = '\ufeff' + self.fields[0]

        return self.fields


class CSVBuffer:
    def write(self, value):
        return value


class CSVStream:
    def export(self, filename, data):
        writer = csv.writer(CSVBuffer())

        response = StreamingHttpResponse((writer.writerow(row) for row in data),
                                         content_type="text/csv")

        response['Content-Disposition'] = f"attachment; filename={filename}.csv"
        return response

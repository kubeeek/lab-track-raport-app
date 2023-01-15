import csv
from django.http import StreamingHttpResponse

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
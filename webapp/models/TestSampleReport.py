from django.db import models

from webapp.models import TestSample
from webapp.models.common import ModelWithTimestamp


class TestSampleReport(ModelWithTimestamp):
    test_sample = models.OneToOneField(TestSample, editable=False, on_delete=models.CASCADE, related_name="report")
    author = models.JSONField()
    supplier_name = models.CharField(max_length=128)
    supplier_address = models.CharField(max_length=128)
    receiver_name = models.CharField(max_length=128)
    receiver_address = models.CharField(max_length=128)
    mechanism_name = models.CharField(max_length=128)
    contract_id = models.CharField(max_length=128)

    transport_method_choices = [
        ('M1', 'Method 1'),
        ('M2', 'Method 2'),
    ]
    transport_method = models.CharField(choices=transport_method_choices, max_length=4)

    def get_formatted_author_list(self):
        authors = filter(lambda element: 'first_name' in element and element['first_name'] is not None, self.author)

        list_output = list(map(lambda element: f'{element.get("first_name")} {element.get("last_name")}', authors))

        return list_output

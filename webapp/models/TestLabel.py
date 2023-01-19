from django.db import models

from webapp.models import TestSample
from webapp.models.common import ModelWithTimestamp

label_type_choices = [
    ('FC', 'Fizykochemiczne'),
    ('OG', 'Organoleptyczne')
]


class TestLabel(ModelWithTimestamp):
    test_sample = models.ForeignKey(TestSample, on_delete=models.PROTECT, editable=False, default=None)

    is_done = models.BooleanField(default=False)
    parameter_name = models.CharField(max_length=128)
    labeling = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    specification = models.CharField(max_length=255)
    # rozporządzenie ?
    regulation = models.CharField(max_length=255)
    sample_amount = models.IntegerField()
    test_result = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    # label type
    type = models.CharField(max_length=10, choices=label_type_choices)
    method_status = models.CharField(max_length=255)
    uncertainty = models.CharField(max_length=255)
    LOD = models.CharField(max_length=255)
    LOQ = models.CharField(max_length=255)

    def get_absolute_url(self):
        return "/test-label/%i/" % self.id

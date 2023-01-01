from django.db import models

from webapp.models import TestingFacility


class TestSample(models.Model):
    sample_code = models.CharField(max_length=16)
    source_facility = models.ForeignKey(TestingFacility, on_delete=models.PROTECT, default=None)
    description = models.TextField()
    admission_date = models.DateField()
    expiration_date = models.DateField()
    expiration_date_optional = models.TextField()
    test_end_date = models.DateField()
    sample_size = models.CharField(max_length=32)
    customer_name = models.CharField(max_length=32)
    appeal_test = models.BooleanField()
    control_type = models.CharField(
        max_length=128,
        default='Bez zastrzezen'
    )
    sample_type_choices = [
        ('T1', 'Type 1'),
        ('T2', 'Type 2'),
    ]
    sample_type = models.CharField(
        max_length=3,
        choices=sample_type_choices,
        default='T2'
    )

    def get_absolute_url(self):
        return "/test-sample/%i/" % self.id
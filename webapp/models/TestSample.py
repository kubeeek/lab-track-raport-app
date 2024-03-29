import datetime

from django.db import models

from webapp.models import TestingFacility
from webapp.models.common import ModelWithTimestamp

# moved outside class because it needs to be reused somewhere else
sample_type_choices = [
    ('T1', 'Type 1'),
    ('T2', 'Type 2'),
]


class TestSample(ModelWithTimestamp):
    sample_code = models.CharField(max_length=16)
    source_facility = models.ForeignKey(TestingFacility, on_delete=models.PROTECT, default=None)
    customer_name = models.CharField(max_length=255)
    description = models.TextField()
    admission_date = models.DateField(default=datetime.date.today)
    expiration_date = models.DateField()
    expiration_date_optional = models.TextField(default=None, null=True, blank=True)
    test_end_date = models.DateField(default=datetime.date.today)
    sample_size = models.CharField(max_length=32)
    appeal_test = models.BooleanField()
    sample_condition = models.CharField(
        max_length=128,
        default="Bez zastrzezeń"
    )

    # sample type
    type = models.CharField(
        max_length=3,
        choices=sample_type_choices,
        default='T2'
    )

    sample_method_choices = [
        ('T1', 'Type 1'),
        ('T2', 'Type 2'),
    ]
    sample_method = models.CharField(
        max_length=128,
        choices=sample_type_choices,
        default='T2'
    )

    class Meta:
        ordering = ['id']
        get_latest_by = ['created_at']

    def get_absolute_url(self):
        return "/test-sample/%i/" % self.id

    def serialize(self):
        model_fields = [field.name for field in self._meta.get_fields(include_parents=True, include_hidden=False)]

        exclude = ['testlabel', 'report']
        data = []
        for field in model_fields:
            if field in exclude:
                continue
            data.append(self.serializable_value(field))
        return data

    def __str__(self):
        return f'Próbka {self.sample_code} nr. {self.id}'

from django.db import models

from webapp.models import TestingFacility
class TestSample(models.Model):
    sample_code = models.CharField(max_length=16)
    source_facility = models.ForeignKey(TestingFacility, on_delete=models.PROTECT, default=None)
    customer_name = models.CharField(max_length=32)
    description = models.TextField()
    admission_date = models.DateField()
    expiration_date = models.DateField()
    expiration_date_optional = models.TextField(default=None, null=True, blank=True)
    test_end_date = models.DateField()
    sample_size = models.CharField(max_length=32)
    appeal_test = models.BooleanField()
    sample_condition = models.CharField(
        max_length=128,
        default="Bez zastrzezeń"
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
    sample_method = models.CharField(
        max_length=128,
        choices=sample_type_choices,
        default='T2'
    )

    class Meta:
        ordering = ['id']
    def get_absolute_url(self):
        return "/test-sample/%i/" % self.id

    def serialize(self):
        model_fields = [field.name for field in self._meta.get_fields(include_parents=True, include_hidden=False)]

        exclude = ['testlabel']
        data = []
        for field in model_fields:
            if field in exclude:
                continue
            data.append(self.serializable_value(field))
        return data


    def __str__(self):
        return f'Próbka {self.sample_code} nr. {self.id}'
import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

from webapp.models import TestSample
from webapp.models.common import ModelWithTimestamp

# moved outside class because it needs to be reused somewhere else
label_type_choices = [
    ('FC', 'Fizykochemiczne'),
    ('OG', 'Organoleptyczne')
]


class TestLabel(ModelWithTimestamp):
    test_sample = models.ForeignKey(TestSample, on_delete=models.PROTECT, editable=False, default=None)

    is_done = models.BooleanField(default=False)
    parameter_name = models.CharField(max_length=128)
    value = models.CharField(max_length=255)
    labeling = models.CharField(max_length=255, blank=True, null=True, default=None)
    specification = models.CharField(max_length=255, blank=True, null=True, default=None)
    # rozporządzenie ?
    regulation = models.CharField(max_length=255, blank=True, null=True, default=None)
    sample_amount = models.IntegerField()
    test_result = models.CharField(max_length=255)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    # label type
    type = models.CharField(max_length=10, choices=label_type_choices)
    method_status = models.CharField(max_length=255)
    uncertainty = models.CharField(max_length=255)
    LOD = models.CharField(max_length=255)
    LOQ = models.CharField(max_length=255)

    def get_absolute_url(self):
        return "/test-label/%i/" % self.id

    def clean(self):
        if not self.regulation and not self.specification and not self.labeling:
            raise ValidationError(
                "Conajmniej jedno z pól (specyfikacja, rozporządzenie, oznakowanie) musi zostać uzupełnione."
            )

    def serialize(self):
        model_fields = [field.name for field in self._meta.get_fields(include_parents=True, include_hidden=False)]

        data = []
        for field in model_fields:
            data.append(self.serializable_value(field))
        return data

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                        Q(specification__isnull=False) |
                        Q(labeling__isnull=False) |
                        Q(regulation__isnull=False)
                ),
                name='one_of_three_required',
            )
        ]

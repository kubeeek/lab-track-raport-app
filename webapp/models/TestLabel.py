from django.db import models

from webapp.models import TestSample


class TestLabel(models.Model):
    done = models.BooleanField(default=False)
    parameter_name = models.CharField(max_length=128)
    test_sample = models.ForeignKey(TestSample, on_delete=models.PROTECT, default=None)

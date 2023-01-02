from django.db import models


class TestingFacility(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}, {self.address}'

from django.db import models


class TestingFacility(models.Model):
    place_code = models.CharField(max_length=32)

    def __str__(self):
        return self.place_code

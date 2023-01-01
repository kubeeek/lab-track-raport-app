from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from webapp.models import TestSample, TestLabel


class TestSampleForm(ModelForm):
    class Meta:
        fields = '__all__'


TestSampleFormset = inlineformset_factory(
    TestSample, TestLabel, exclude=['done'], extra=1, can_delete=False
)

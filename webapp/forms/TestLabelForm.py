from django.forms import ModelForm

from webapp.models import TestLabel


class TestSampleUpdateForm(ModelForm):
    class Meta:
        model = TestLabel
        fields = '__all__'
        exclude = ('test_sample',)

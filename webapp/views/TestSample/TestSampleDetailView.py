from django.views.generic.detail import DetailView

from webapp.models import TestSample, TestLabel


class TestSampleDetailView(DetailView):
    model = TestSample

    # pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['testlabel_list'] = TestLabel.objects.filter(test_sample=self.get_object())
        context['has_report'] = hasattr(self.object, 'report')

        return context

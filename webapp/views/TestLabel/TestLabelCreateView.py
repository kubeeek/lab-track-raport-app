from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.http import Http404

from webapp.forms import TestLabelForm
from webapp.models import TestLabel, TestSample
from webapp.views.common import OperationSuccessMessageViewMixin


class TestLabelCreateView(OperationSuccessMessageViewMixin, CreateView):
    form_class = TestLabelForm
    model = TestLabel

    def get_initial(self):
        return {
            'test_sample': TestSample.objects.get(pk=self.kwargs['pk'])
        }

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except TestSample.DoesNotExist:
            raise Http404

        context['parent'] = get_object_or_404(TestSample, pk=self.kwargs['pk'])

        return context

    def form_valid(self, form):
        parent = get_object_or_404(TestSample, pk=self.kwargs['pk'])
        self.success_url = parent.get_absolute_url()
        form.instance.test_sample = parent
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url

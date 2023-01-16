from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from webapp.models import TestSample


class NestedCreateView(CreateView):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.parentModel = None
        self.parentInstance = None

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except TestSample.DoesNotExist:
            raise Http404

        context['parent'] = get_object_or_404(self.parentModel, pk=self.kwargs['pk'])

        return context

    def get_parent_instance(self):
        self.parentInstance = get_object_or_404(self.parentModel, pk=self.kwargs['pk'])
        self.success_url = self.parentInstance.get_absolute_url()

        return self.parentInstance

    def get_success_url(self):
        return self.success_url

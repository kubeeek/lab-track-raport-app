from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import DeleteView

from webapp.models import TestSample
from webapp.views.common import OperationSuccessMessageViewMixin


class TestSampleDeleteView(OperationSuccessMessageViewMixin, DeleteView):
    model = TestSample
    success_url = reverse_lazy('testsample_list')

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, args, kwargs)
            return redirect(self.get_success_url())
        except ProtectedError:
            messages.error(request, "Nie można usunąć próbki. Najpierw usuń przypisane do niego badania.")
            return redirect(reverse('testsample_detail', kwargs={'pk': self.object.id}))

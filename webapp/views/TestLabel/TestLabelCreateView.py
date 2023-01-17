from webapp.forms import TestLabelForm
from webapp.models import TestLabel, TestSample
from webapp.views.common import NestedCreateView
from webapp.views.common import OperationSuccessMessageViewMixin


class TestLabelCreateView(OperationSuccessMessageViewMixin, NestedCreateView):
    form_class = TestLabelForm
    model = TestLabel

    parentModel = TestSample

    def get_initial(self):
        return {
            'test_sample': self.parentModel.objects.get(pk=self.kwargs['pk'])
        }

    def form_valid(self, form):
        form.instance.test_sample = self.get_parent_instance()
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url

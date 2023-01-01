from django.views.generic import CreateView

from webapp.models import TestLabel, TestSample


class TestLabelCreateView(CreateView):
    fields = '__all__'
    model = TestLabel

    def get_form(self, **kwargs):
        form = super().get_form()

        form.fields['test_sample'].disabled = True
        return form

    def get_initial(self):
        return {
            'test_sample': self.kwargs["pk"]
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['parent'] = TestSample.objects.get(pk=self.kwargs['pk'])

        return context

    def form_valid(self, form):
        parent = form.cleaned_data['test_sample']
        self.success_url = parent.get_absolute_url()

        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url

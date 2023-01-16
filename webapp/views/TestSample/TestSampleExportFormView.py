from django.urls import reverse

from webapp.views.common.ExportFormView import ExportFormView


class TestSampleExportFormView(ExportFormView):
    def get_context_data(self, **kwargs):
        context = super(TestSampleExportFormView, self).get_context_data(**kwargs)

        context['submit_url'] = reverse('test_sample_export_download')
        context['header'] = "Próbki"

        return context

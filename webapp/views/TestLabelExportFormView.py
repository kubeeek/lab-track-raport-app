from django.urls import reverse

from webapp.views.common.ExportFormView import ExportFormView


class TestLabelExportFormView(ExportFormView):
    def get_context_data(self, **kwargs):
        context = super(TestLabelExportFormView, self).get_context_data(**kwargs)

        context['submit_url'] = reverse('test_label_export_download')
        context['header'] = "Zlecone badania"

        return context

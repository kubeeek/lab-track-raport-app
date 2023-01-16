import os

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import DetailView
from docxtpl import DocxTemplate

from webapp.models import TestSampleReport, TestSample


class TestSampleReportDownloadView(DetailView):
    model = TestSampleReport

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

        test_report = self.object
        related_test_sample = TestSample.objects.get(id=test_report.test_sample.id)

        tpl = DocxTemplate(os.path.join(settings.BASE_DIR, 'webapp/templates/webapp/report_template.docx'))
        tpl.render(
            {
                'supplier_name':test_report.supplier_name,
                'receiver_name': test_report.receiver_name,
                'contract_id': test_report.contract_id,
                'admission_date': related_test_sample.admission_date,
                'sample_description': related_test_sample.description,
                'sample_size': related_test_sample.sample_size,
                'sample_condition': related_test_sample.sample_condition
            }

        )

        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        response["Content-Disposition"] = f'filename="sprawozdanie próbka {related_test_sample.sample_code}.docx"'

        tpl.save(response)

        return response

import os

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import DetailView
from docxtpl import DocxTemplate

from webapp.models import TestSampleReport, TestSample, TestLabel


class TestSampleReportDownloadView(DetailView):
    model = TestSampleReport

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

        test_report = self.object
        related_test_sample = TestSample.objects.get(id=test_report.test_sample.id)
        related_test_labels = list(related_test_sample.testlabel_set.all())

        tpl = DocxTemplate(os.path.join(settings.BASE_DIR, 'webapp/templates/webapp/report_template.docx'))
        tpl.render(
            {
                'appeal_test': related_test_sample.appeal_test,
                'customer_name': related_test_sample.customer_name,
                'admission_date': related_test_sample.admission_date,
                'supplier_name':test_report.supplier_name,
                'receiver_name': test_report.receiver_name,
                'contract_id': test_report.contract_id,
                'expiration_date': related_test_sample.expiration_date,
                'sample_id': related_test_sample.id,
                'sample_code': related_test_sample.sample_code,
                'sample_description': related_test_sample.description,
                'sample_size': related_test_sample.sample_size,
                'sample_method': related_test_sample.sample_method,
                'sample_condition': related_test_sample.sample_condition,
                'tbl_labels': related_test_labels
            }

        )

        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        response["Content-Disposition"] = f'filename="sprawozdanie próbka {related_test_sample.sample_code}.docx"'

        tpl.save(response)

        return response

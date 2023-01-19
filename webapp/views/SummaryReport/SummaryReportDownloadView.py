import os

from django.conf import settings
from django.db.models import Count
from django.http import HttpResponse
from django.views.generic import View
from docxtpl import DocxTemplate

from webapp.models import TestSample, sample_type_choices, label_type_choices
from .common import preprocess_data, get_data_for_report


class SummaryReportDownloadView(View):

    def get(self, request, *args, **kwargs):
        if 'summary_range' not in request.session:
            # 204 no content
            return HttpResponse(status=204)

        from_date = request.session['summary_range'][0]
        to_date = request.session['summary_range'][1]

        [testsample_data, total_samples, testlabel_data, total_labels] = get_data_for_report({ 'from_date': from_date, 'to_date': to_date})

        preprocess_data([(testsample_data, sample_type_choices), (testlabel_data, label_type_choices)])

        tpl = DocxTemplate(os.path.join(settings.BASE_DIR, 'webapp/templates/webapp/summary_template.docx'))
        tpl.render(
            {
                'tbl_samples': testsample_data,
                'total_testsample': total_samples,
                'tbl_labels': testlabel_data,
                'total_labels': total_labels,
                'from_date': from_date,
                'to_date': to_date
            }

        )

        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        response["Content-Disposition"] = f'filename="raport {from_date} - {to_date}.docx"'

        tpl.save(response)

        return response

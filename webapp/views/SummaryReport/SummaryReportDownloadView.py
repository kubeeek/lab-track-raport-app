import os

from django.conf import settings
from django.db.models import Count
from django.http import HttpResponse
from django.views.generic import View
from docxtpl import DocxTemplate

from webapp.models import TestSample


class SummaryReportDownloadView(View):

    def get(self, request, *args, **kwargs):
        if 'summary_range' not in request.session:
            # 204 no content
            return HttpResponse(status=204)

        from_date = request.session['summary_range'][0]
        to_date = request.session['summary_range'][1]

        testsample_filtered = TestSample.objects.filter(
            admission_date__range=[from_date, to_date]).all()

        testsample_data = list(
            testsample_filtered.values('sample_type').annotate(dcount=Count('sample_type')).order_by())

        total_testsample = testsample_filtered.count()

        tpl = DocxTemplate(os.path.join(settings.BASE_DIR, 'webapp/templates/webapp/summary_template.docx'))
        tpl.render(
            {
                'tbl_samples': testsample_data,
                'total_testsample': total_testsample,
                'from_date': from_date,
                'to_date': to_date
            }

        )

        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        response["Content-Disposition"] = f'filename="raport {from_date} - {to_date}.docx"'

        tpl.save(response)

        return response

import urllib

from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse, resolve
from django.views.generic import FormView

from webapp.forms import SummaryReportForm
from webapp.models import TestSample, sample_type_choices
from webapp.utils.decorators import parse_timestamp_range


class SummaryReportView(FormView):
    template_name = "webapp/summary_report_form.html"
    form_class = SummaryReportForm

    def get_initial(self):
        initial = super().get_initial()

        if 'from_date' in self.request.GET:
            initial['from_date'] = self.request.GET['from_date']

        if 'to_date' in self.request.GET:
            initial['to_date'] = self.request.GET['to_date']

        return initial

    @parse_timestamp_range()
    def get(self, request, filter_params, *args, **kwargs):

        if bool(request.GET) and filter_params is None:
            filter_params = {
                'from_date': TestSample.objects.earliest().created_at.strftime('%Y-%m-%d'),
                'to_date': TestSample.objects.latest().created_at.strftime('%Y-%m-%d')
            }

            resolution = resolve(request.path_info)  # simulate resolving the request

            reversed = reverse(resolution.url_name, kwargs=resolution.kwargs)  # create a base url

            reversed += '?' + urllib.parse.urlencode(filter_params)

            return HttpResponseRedirect(reversed)
        else:
            return super().get(request)

    def get_data(self, filter_params):

        testsample_filtered = TestSample.objects.filter(
            admission_date__range=[filter_params['from_date'], filter_params['to_date']]).all()

        testsample_data = list(
            testsample_filtered.values('sample_type').annotate(dcount=Count('sample_type')).order_by())

        total_testsample = testsample_filtered.count()

        # make human readable labels
        for entry in testsample_data:
            key = entry['sample_type']
            for choice in sample_type_choices:
                if choice[0] == key:
                    entry['sample_type'] = choice[1]
                    break

        return [filter_params, testsample_data, total_testsample]

    @parse_timestamp_range()
    def get_context_data(self, filter_params, **kwargs):
        context = super().get_context_data()

        if not bool(self.request.GET):
            return context

        data = self.get_data(filter_params)

        context['date_range'] = data[0]
        context['test_samples'] = data[1]
        context['total_samples'] = data[2]
        context['render_data'] = True

        return context

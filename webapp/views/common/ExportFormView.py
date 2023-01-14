from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from webapp.forms import ExportForm


@method_decorator(csrf_exempt, name='dispatch')
class ExportFormView(FormView):
    template_name = "webapp/export_form.html"
    form_class = ExportForm

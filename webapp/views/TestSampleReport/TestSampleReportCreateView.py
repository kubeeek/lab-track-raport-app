from django.contrib import messages
from django.db import IntegrityError
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import AuthorFormSet, TestSampleReportForm
from webapp.models import TestSampleReport, TestSample


class TestSampleReportCreateView(CreateView):
    model = TestSampleReport
    form_class = TestSampleReportForm

    def get_initial(self):
        return {
            'parent': TestSample.objects.get(pk=self.kwargs['pk'])
        }

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except TestSample.DoesNotExist:
            raise Http404

        context['parent'] = get_object_or_404(TestSample, pk=self.kwargs['pk'])
        context['authors_formset'] = AuthorFormSet()

        return context

    def form_valid(self, form):
        # check related formset
        formset = AuthorFormSet(self.request.POST)

        authors = []

        if formset.is_valid() is False:
            for _form in formset:
                if _form.is_valid():
                    print(form.data)
                else:
                    return render(self.request, self.template_name, {'form': form, 'authors_formset': formset})

        for f in formset:
            cd = f.cleaned_data
            first_name = cd.get('first_name')
            last_name = cd.get('last_name')

            authors.append({"first_name": first_name, "last_name": last_name})

        parent = get_object_or_404(TestSample, pk=self.kwargs['pk'])
        self.success_url = parent.get_absolute_url()
        form.instance.test_sample = parent

        obj_instance = form.save(commit=False)
        obj_instance.author = authors

        try:
            obj_instance.save()
        except IntegrityError:
            messages.error(self.request, "Nie można stworzyć raportu. Dana próbka ma już przypisany raport.")
            return redirect(reverse('testsample_detail', kwargs={'pk': parent.id}))

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.success_url

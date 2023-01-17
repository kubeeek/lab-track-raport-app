from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView

from webapp.forms import TestSampleReportForm, AuthorFormSet
from webapp.models import TestSampleReport
from webapp.views.common import OperationSuccessMessageViewMixin


class TestSampleReportUpdateView(OperationSuccessMessageViewMixin, UpdateView):
    model = TestSampleReport
    form_class = TestSampleReportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # populate existing authors
        authors = self.object.author

        context['authors_formset'] = AuthorFormSet(initial=authors)

        return context

    def form_valid(self, form):
        """
        See TestSampleReportCreateView.py
        """
        # check related formset
        formset = AuthorFormSet(self.request.POST)

        authors = []

        if formset.is_valid() is False:
            form_nested = formset[0]
            if form_nested.is_valid():
                pass
            else:
                return render(self.request, "webapp/testsamplereport_form.html",
                              {'form': form, 'authors_formset': formset})

        for f in formset:
            cd = f.cleaned_data
            first_name = cd.get('first_name')
            last_name = cd.get('last_name')

            if first_name is None or last_name is None:
                continue

            authors.append({"first_name": first_name, "last_name": last_name})

        form.instance.test_sample = self.object.test_sample

        obj_instance = form.save(commit=False)
        obj_instance.author = authors

        try:
            obj_instance.save()
        except IntegrityError:
            messages.error(self.request, "Coś poszło nie tak. Dana próbka ma już przypisany raport.")
            return redirect(reverse('testsample_detail', kwargs={'pk': self.parentInstance.id}))

        return HttpResponseRedirect(self.object.test_sample.get_absolute_url())

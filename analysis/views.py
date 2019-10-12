from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from analysis import models


class AnalysisListView(PermissionRequiredMixin, ListView):
    model = models.Analysis
    permission_required = 'analysis.view_analysis'
    login_url = reverse_lazy('custom_auth:login')


class AnalysisView(PermissionRequiredMixin, DetailView):
    model = models.Analysis
    permission_required = 'analysis.view_analysis'
    pk_url_kwarg = 'analysis_id'


class AnalysisCreateView(PermissionRequiredMixin, CreateView):
    model = models.Analysis
    permission_required = 'analysis.add_analysis'
    fields = ('name', 'description')

    def get_context_data(self, **kwargs):
        context = super(AnalysisCreateView, self).get_context_data()
        context['action'] = 'Create'
        context['description'] = 'Create Analysis for your companies.'
        return context

    def get_success_url(self):
        messages.success(self.request, 'The Analysis with name: "%s" has been created.' % self.object.name.title())
        return reverse_lazy('analysis:analysis', kwargs={'analysis_id': self.object.pk})


class AnalysisEditView(PermissionRequiredMixin, UpdateView):
    model = models.Analysis
    permission_required = 'analysis.change_analysis'
    fields = ('name', 'description')
    pk_url_kwarg = 'analysis_id'

    def get_context_data(self, **kwargs):
        context = super(AnalysisEditView, self).get_context_data()
        context['action'] = 'Update'
        context['description'] = "Update Analysis if it's required."
        return context

    def get_success_url(self):
        messages.success(self.request, 'The Analysis with name: "%s" has been updated.' % self.object.name.title())
        return reverse_lazy('analysis:analysis', kwargs={'analysis_id': self.object.pk})


class AnalysisDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Analysis
    permission_required = 'analysis.delete_analysis'
    pk_url_kwarg = 'analysis_id'
    success_url = reverse_lazy('analysis:analysis_list')

    def get_success_url(self):
        messages.success(self.request, 'The Analysis with name: "%s" has been deleted.' % self.object.name.title())
        return super(AnalysisDeleteView, self).get_success_url()

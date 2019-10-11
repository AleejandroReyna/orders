from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from analysis_parameters import models
from django.urls import reverse_lazy
from django.contrib import messages


class ParameterListView(PermissionRequiredMixin, ListView):
    model = models.Parameter
    permission_required = 'analysis_parameters.view_parameter'


class ParameterView(PermissionRequiredMixin, DetailView):
    model = models.Parameter
    pk_url_kwarg = 'parameter_id'
    permission_required = 'analysis_parameters.view_parameter'


class ParameterCreateView(PermissionRequiredMixin, CreateView):
    model = models.Parameter
    permission_required = 'analysis_parameters.add_parameter'
    fields = ('name', 'description', 'category', 'type')

    def get_context_data(self, **kwargs):
        context = super(ParameterCreateView, self).get_context_data()
        context['action'] = 'Create'
        context['description'] = 'Add a parameter for your analysis'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.name = form.instance.name.lower()
        return super(ParameterCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'The parameter with name: "%s" for category: %s has been created' % (
            self.object.name.title(), self.object.category.name.title()
        ))
        return reverse_lazy('parameters:parameter', kwargs={'parameter_id': self.object.pk})


class ParameterEditView(PermissionRequiredMixin, UpdateView):
    model = models.Parameter
    permission_required = 'analysis_parameters.change_parameter'
    pk_url_kwarg = 'parameter_id'
    fields = ('name', 'description', 'category', 'type')

    def get_context_data(self, **kwargs):
        context = super(ParameterEditView, self).get_context_data()
        context['action'] = 'Edit'
        context['description'] = 'Edit the parameter section'
        return context

    def get_success_url(self):
        messages.success(self.request, 'The parameter with name: "%s" has been updated' % self.object.name.title())
        return reverse_lazy('parameters:parameter', kwargs={'parameter_id': self.object.pk})


class ParameterDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Parameter
    permission_required = 'analysis_parameters.delete_parameter'
    pk_url_kwarg = 'parameter_id'

    def get_context_data(self, **kwargs):
        context = super(ParameterDeleteView, self).get_context_data()
        context['description'] = 'Are you sure to delete the parameter with name: %s?' % self.object.name.title()
        return context

    def get_success_url(self):
        messages.success(self.request, "Parameter with name: %s has been deleted." % self.object.name.title())
        return reverse_lazy('parameters:parameters')

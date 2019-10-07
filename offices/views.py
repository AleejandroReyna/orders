from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from companies import models
from django.contrib import messages


class OfficeCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = models.Office
    template_name = 'offices/office_form.html'
    fields = ('name', 'company', 'phone', 'address')
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.add_office'

    def form_valid(self, form):
        messages.success(self.request, 'Company has been added', extra_tags='success')
        return super(OfficeCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('offices:office', kwargs={'office_id': self.object.pk})

    def get_form(self, form_class=None):
        form = super(OfficeCreateView, self).get_form()
        form.fields['company'].queryset = self.request.user.company_set.all()
        return form

    def get_context_data(self, **kwargs):
        context = super(OfficeCreateView, self).get_context_data()
        context['action'] = 'Create'
        return context


class OfficeEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = models.Office
    template_name = 'offices/office_form.html'
    fields = ('name', 'phone', 'address')
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.change_office'
    pk_url_kwarg = 'office_id'

    def get_context_data(self, **kwargs):
        context = super(OfficeEditView, self).get_context_data()
        context['action'] = 'Edit'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Office with id %s has been updated' % self.object.pk, extra_tags='success')
        return super(OfficeEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('offices:office', kwargs={'office_id': self.object.pk})


class OfficeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Office
    template_name = 'offices/office_form.html'
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    pk_url_kwarg = 'office_id'
    permission_required = 'companies.delete_office'

    def get_context_data(self, **kwargs):
        context = super(OfficeDeleteView, self).get_context_data()
        context['description'] = 'Are you sure to delete office with name: "%s"?' % self.object.name
        context['action'] = 'Delete'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Office has deleted')
        return super(OfficeDeleteView, self).delete()


class OfficeView(DetailView):
    pk_url_kwarg = 'office_id'
    model = models.Office
    template_name = 'offices/office_single.html'

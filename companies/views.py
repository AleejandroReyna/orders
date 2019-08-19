from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from companies import models
from django.urls import reverse_lazy
from django.contrib.messages import success


class CompanyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Company
    fields = ('name', 'address', 'phone', 'description')
    template_name_suffix = '_form'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.add_company'
    permission_denied_message = 'Unauthorized'
    success_url = reverse_lazy('companies:list_company')

    def form_valid(self, form):
        success(self.request, 'Company has been added', extra_tags='success')
        return super(CompanyCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CompanyCreateView, self).get_context_data()
        context['action'] = 'Create'
        return context


class CompanyListView(ListView):
    model = models.Company
    paginate_by = 10
    template_name_suffix = '_list'

    def get_queryset(self):
        queryset = self.request.user.company_set.all()
        return queryset


class CompanyView(DetailView):
    template_name_suffix = '_single'
    model = models.Company
    pk_url_kwarg = 'company_id'


class CompanyEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Company
    fields = ('name', 'address', 'phone', 'description')
    template_name_suffix = '_form'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.add_company'
    pk_url_kwarg = 'company_id'

    def get_context_data(self, **kwargs):
        context = super(CompanyEditView, self).get_context_data()
        context['action'] = 'Edit'
        return context

    def form_valid(self, form):
        success(self.request, 'Company has been updated', extra_tags='success')
        return super(CompanyEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('companies:company', kwargs={'company_id': self.kwargs['company_id']})


class CompanyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Company
    pk_url_kwarg = 'company_id'
    success_url = reverse_lazy('companies:list_company')
    template_name_suffix = '_form'
    permission_required = 'companies.delete_company'

    def delete(self, request, *args, **kwargs):
        success(request, 'Company has deleted')
        return super(CompanyDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CompanyDeleteView, self).get_context_data()
        context['action'] = 'Delete'
        context['description'] = 'Are you sure to delete the company with name: "%s"?' % self.object.name
        return context


class CreateCompanyOfficeView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Office
    fields = ('name', 'phone', 'address')
    template_name = 'offices/office_form.html'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.add_office'
    permission_denied_message = 'Unauthorized'
    success_url = reverse_lazy('companies:list_company')

    def form_valid(self, form):
        success(self.request, 'Company has been added', extra_tags='success')
        form.instance.company_id = self.kwargs['company_id']
        return super(CreateCompanyOfficeView, self).form_valid(form)


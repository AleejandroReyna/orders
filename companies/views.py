from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from companies import models
from django.urls import reverse_lazy
from django.contrib import messages


class CompanyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Company
    fields = ('name', 'address', 'phone', 'description', 'nit')
    template_name_suffix = '_form'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.add_company'
    permission_denied_message = 'Unauthorized'
    success_url = reverse_lazy('companies:list_company')

    def get_context_data(self, **kwargs):
        context = super(CompanyCreateView, self).get_context_data()
        context['action'] = 'Create'
        context['description'] = 'Create a company for active user.'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Company has been added', extra_tags='success')
        return super(CompanyCreateView, self).get_success_url()


class CompanyListView(ListView):
    model = models.Company
    paginate_by = 10
    template_name_suffix = '_list'

    def get_queryset(self):
        queryset = self.request.user.company_set.all()
        return queryset


class CompanyView(DetailView):
    model = models.Company
    pk_url_kwarg = 'company_id'

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data()
        company = models.Company.objects.get(pk=context['object'].pk)
        role = models.CompanyRole.objects.get(name='client')
        context['clients'] = company.users.filter(companyuserrole__company_role=role)
        return context


class CompanyEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Company
    fields = ('name', 'address', 'phone', 'description', 'nit')
    template_name_suffix = '_form'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.add_company'
    pk_url_kwarg = 'company_id'

    def get_context_data(self, **kwargs):
        context = super(CompanyEditView, self).get_context_data()
        context['action'] = 'Edit'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Company has been updated', extra_tags='success')
        return reverse_lazy('companies:company', kwargs={'company_id': self.kwargs['company_id']})


class CompanyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Company
    pk_url_kwarg = 'company_id'
    template_name_suffix = '_form'
    permission_required = 'companies.delete_company'

    def get_context_data(self, **kwargs):
        context = super(CompanyDeleteView, self).get_context_data()
        context['action'] = 'Delete'
        context['description'] = 'Are you sure to delete the company with name: "%s"?' % self.object.name
        return context

    def get_success_url(self):
        messages.success(self.request, 'Company has deleted')
        return reverse_lazy('companies:list_company')


class CreateCompanyOfficeView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Office
    fields = ('name', 'phone', 'address')
    template_name = 'offices/office_form.html'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.add_office'
    permission_denied_message = 'Unauthorized'

    def form_valid(self, form):
        form.instance.company_id = self.kwargs['company_id']
        return super(CreateCompanyOfficeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateCompanyOfficeView, self).get_context_data()
        context['action'] = 'Create'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Office with name: "%s" has been added.' % self.object.name,
                         extra_tags='success')
        return reverse_lazy('offices:office', kwargs={'office_id': self.object.pk})

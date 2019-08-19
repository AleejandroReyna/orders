from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from companies import models
from django.urls import reverse_lazy
from django.contrib.messages import success


class CreateCompanyView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Company
    fields = ('name', 'address', 'phone', 'description')
    template_name_suffix = '_create_form'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.add_company'
    permission_denied_message = 'Unauthorized'
    success_url = reverse_lazy('companies:list_company')

    def form_valid(self, form):
        success(self.request, 'Company has been added', extra_tags='success')
        return super(CreateCompanyView, self).form_valid(form)


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


class CreateOfficeView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Office
    fields = ('name', 'company', 'phone', 'address')
    template_name_suffix = '_office_form'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.add_office'
    permission_denied_message = 'Unauthorized'
    success_url = reverse_lazy('companies:list_company')

    def form_valid(self, form):
        success(self.request, 'Company has been added', extra_tags='success')
        return super(CreateOfficeView, self).form_valid()

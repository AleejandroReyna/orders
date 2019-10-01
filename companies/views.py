from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from companies import models
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404


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
    template_name_suffix = '_single'
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


class CompanyExamsListView(PermissionRequiredMixin, ListView):
    model = models.CompanyExamAssociation
    permission_required = 'companies.view_companyexamassociation'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_denied_message = 'Unauthorized'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CompanyExamsListView, self).get_context_data()
        context['company'] = get_object_or_404(models.Company, id=self.kwargs['company_id'])
        return context


class CreateCompanyExamAssociationView(PermissionRequiredMixin, CreateView):
    model = models.CompanyExamAssociation
    permission_required = 'companies.add_companyexamassociation'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_denied_message = 'Unauthorized'
    fields = ('exam',)

    def get_context_data(self, **kwargs):
        context = super(CreateCompanyExamAssociationView, self).get_context_data()
        context['action'] = 'Create'
        context['company'] = get_object_or_404(models.Company, id=self.kwargs['company_id'])
        context['form'].fields['exam'].queryset = models.Exam.objects.exclude(company=context['company'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.company_id = self.kwargs['company_id']
        return super(CreateCompanyExamAssociationView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Exam with name: "%s" has been added to company: "%s".' % (self.object.exam,
                                                                                                  self.object.company))
        return reverse_lazy('companies:list_company_exams', kwargs={'company_id': self.object.company.pk})


class CreateCompanyExamAssociationValueView(PermissionRequiredMixin, CreateView):
    model = models.CompanyExamAssociationValue
    fields = ('type',)
    permission_required = 'companies.add_companyexamassociationvalue'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'

    def get_form(self, form_class=None):
        form = super(CreateCompanyExamAssociationValueView, self).get_form()
        association = get_object_or_404(models.CompanyExamAssociation, id=self.kwargs['exam_association_id'])
        form.fields['type'].initial = association.exam.type
        return form

    def get_context_data(self, **kwargs):
        context = super(CreateCompanyExamAssociationValueView, self).get_context_data(**kwargs)
        context['action'] = 'Create'
        association = get_object_or_404(models.CompanyExamAssociation, id=self.kwargs['exam_association_id'])
        context['company'] = association.company
        context['exam'] = association.exam
        return context

    def form_valid(self, form):
        association = get_object_or_404(models.CompanyExamAssociation, id=self.kwargs['exam_association_id'])
        form.instance.user = self.request.user
        form.instance.company_exam_association = association
        return super(CreateCompanyExamAssociationValueView, self).form_valid(form)

    def get_success_url(self):
        association = get_object_or_404(models.CompanyExamAssociation, id=self.kwargs['exam_association_id'])
        messages.success(self.request, 'Type added for association for company: "%s" and Exam: %s' %
                         (association.company.name.title(), association.exam.name.title()))
        return reverse_lazy('companies:list_company_exams', kwargs=dict(company_id=association.company.pk))


class EditCompanyExamAssociationValueTypeStaticView(PermissionRequiredMixin, UpdateView):
    model = models.CompanyExamAssociationValue
    fields = ('response_type_group',)
    permission_required = 'companies.change_companyexamassociationvalue'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    pk_url_kwarg = 'exam_association_value_id'

    def get_context_data(self, **kwargs):
        context = super(EditCompanyExamAssociationValueTypeStaticView, self).get_context_data()
        context['company'] = self.object.company_exam_association.company
        context['exam'] = self.object.company_exam_association.exam
        context['action'] = 'Edit'
        return context
    
    def get_initial(self):
        initial = super(EditCompanyExamAssociationValueTypeStaticView, self).get_initial()
        if self.object.type == 'static':
            try:
                initial['response_type_group'] = self.object.response_type_group if self.object.response_type_group.pk \
                    else self.object.company_exam_association.exam.response_type_group.pk
            except Exception as e:
                print(e)
                pass
        return initial

    def get_success_url(self):
        messages.success(self.request, "Company Exam Associations values has been updated.")
        return reverse_lazy('companies:list_company_exams',
                            kwargs=dict(company_id=self.object.company_exam_association.company.pk))


class EditCompanyExamAssociationValueTypeDynamicView(EditCompanyExamAssociationValueTypeStaticView):
    fields = ('unit', 'min', 'max')

    def get_initial(self):
        initial = super(EditCompanyExamAssociationValueTypeDynamicView, self).get_initial()
        print(initial)
        if self.object.type == 'dynamic':
            try:
                initial['unit'] = self.object.unit if self.object.unit else \
                    self.object.company_exam_association.exam.dynamicexamassignation.unit.pk
                initial['min'] = self.object.min if self.object.min else \
                    self.object.company_exam_association.exam.dynamicexamassignation.min
                initial['max'] = self.object.max if self.object.max else \
                    self.object.company_exam_association.exam.dynamicexamassignation.max
            except Exception as e:
                print(e)
                pass
        return initial


class EditCompanyExamAssociationValueView(EditCompanyExamAssociationValueTypeStaticView):
    fields = ('type',)


class CompanyExamAssociationDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.CompanyExamAssociation
    pk_url_kwarg = 'exam_association_id'
    login_url = reverse_lazy('custom_auth:login')
    permission_required = 'companies.delete_companyexamassociationvalue'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        messages.success(self.request, 'Company Exam Association has been deleted.')
        return reverse_lazy('companies:list_company_exams', kwargs=dict(company_id=self.object.company.pk))

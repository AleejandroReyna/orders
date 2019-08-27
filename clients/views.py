from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from clients import forms
from companies.models import Company, CompanyRole, CompanyUserRole
from django.shortcuts import redirect
from django.contrib import messages


class CreateCompanyClientView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'clients/create_client_form.html'
    form_class = forms.CreateClientForm
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'auth.add_user'

    def get_context_data(self, **kwargs):
        context = super(CreateCompanyClientView, self).get_context_data()
        form = forms.CreateClientForm()
        form.fields['company'].queryset = self.request.user.company_set.all()
        context['form'] = form
        return context

    def post(self, request):
        client_form = forms.ClientForm(request.POST)
        if client_form.is_valid():
            client = client_form.save(commit=False)
            username = "%s_%s" % (client.first_name.replace(" ", "_").lower(),
                                  client.last_name.replace(" ", "_").lower())
            possibles = User.objects.filter(username__contains=username).count()
            password = "%s%s123!#" % (client.first_name.title().replace(" ", ""),
                                      client.last_name.title().replace(" ", ""))
            if possibles > 0:
                username = "%s_%s" % (username, possibles)

            client.username = username
            try:
                group = Group.objects.get(name='client')
                company = Company.objects.get(id=request.POST['company'])
                role = CompanyRole.objects.get(name='client')
                client.set_password(password)
                client.save()
                group.user_set.add(client)
                company_role = CompanyUserRole.objects.create(company=company, company_role=role, user=client)
                messages.success(self.request, 'the clent form company: %s with name: %s has been created' % (
                    company.name, "%s %s" % (client.first_name, client.last_name)), extra_tags='success')
                return redirect('companies:company', company_id=company.pk)
            except Exception as e:
                print(e)
                messages.error(self.request, 'Not possible add client for company', extra_tags='danger')
                return super(CreateCompanyClientView, self).get(self.request)


class ClientView(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'client_id'
    template_name = 'clients/client_single.html'
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'

    def get_context_data(self, **kwargs):
        context = super(ClientView, self).get_context_data()
        admin_companies = self.request.user.company_set\
            .filter(companyuserrole__company_role__name__in=['colaborator', 'administrator'])
        context['companies'] = context['user'].company_set\
            .filter(companyuserrole__company_role__name__in=['client'])\
            .filter(id__in=[item.pk for item in admin_companies])
        return context

from django.contrib.auth.mixins import PermissionRequiredMixin
from companies.models import CompanyRole, CompanyUserRole
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from users.models import UserRole, UserToUserRole, User
from django.contrib.auth.models import Group
from users.forms import UserCreationForm
from django.contrib import messages


class CollaboratorCreateView(PermissionRequiredMixin, TemplateView):
    template_name = 'collaborators/collaborator_form.html'
    permission_required = 'users.create_collaborators'

    def get_context_data(self, **kwargs):
        context = super(CollaboratorCreateView, self).get_context_data()
        context['form'] = UserCreationForm(self.request.POST or None)
        context['action'] = 'Create Collaborator'
        context['description'] = 'Form for create a new collaborator for your companies'
        return context

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            role = get_object_or_404(UserRole, name='collaborator')
            company_role = get_object_or_404(CompanyRole, name='collaborator')
            group = get_object_or_404(Group, name='collaborator')
            print(company_role)
            user = form.save()
            user.groups.add(group)
            assignation = UserToUserRole.objects.create(owner=request.user, user=user, role=role)
            print(assignation)
            for company in self.request.user.get_companies():
                company_assignation = CompanyUserRole.objects.create(user=user, company=company,
                                                                     company_role=company_role)
                print(company_assignation)
            messages.success(self.request, "Your collaborator has been added.")
            return redirect('dashboard:dashboard')
        messages.error(self.request, "Verify your data and try again")
        return super(CollaboratorCreateView, self).get(self.request)


class UserCollaboratorsListView(PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.view_collaborators'
    template_name = 'collaborators/collaborator_list.html'

    def get_queryset(self):
        return self.request.user.get_collaborators()

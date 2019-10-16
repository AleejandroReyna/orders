from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from users.models import UserRole, UserToUserRole, User
from users.forms import UserCreationForm
from django.contrib import messages


class CollaboratorCreateView(PermissionRequiredMixin, TemplateView):
    template_name = 'collaborators/collaborator_form.html'
    permission_required = 'users.add_user'

    def get_context_data(self, **kwargs):
        context = super(CollaboratorCreateView, self).get_context_data()
        context['form'] = UserCreationForm(self.request.GET or None)
        context['action'] = 'Create Collaborator'
        context['description'] = 'Form for create a new collaborator for your companies'
        return context

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            role = get_object_or_404(UserRole, name='collaborator')
            user = form.save()
            assignation = UserToUserRole.objects.create(owner=request.user, user=user, role=role)
            messages.success(self.request, "Your collaborator has been added.")
            return redirect('dashboard:dashboard')
        return super(CollaboratorCreateView, self).get(self.request)


class UserCollaboratorsListView(PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.add_user'
    template_name = 'collaborators/collaborator_list.html'

    def get_queryset(self):
        return self.request.user.get_collaborators()

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from users.models import UserRole, UserToUserRole, User
from clients.forms import CreateClientForm
from users.forms import UserCreationForm
from django.contrib import messages


class UserClientsListView(PermissionRequiredMixin, ListView):
    permission_required = 'users.view_clients'
    model = User
    template_name = 'clients/my_clients_list.html'

    def get_queryset(self):
        return self.request.user.get_clients()


class ClientCreateView(PermissionRequiredMixin, TemplateView):
    template_name = 'clients/client_form.html'
    permission_required = 'users.create_clients'

    def get_context_data(self, **kwargs):
        context = super(ClientCreateView, self).get_context_data()
        context['form'] = CreateClientForm(self.request.POST or None)
        context['action'] = 'Create Client'
        context['form'].fields['user'].queryset = self.request.user.get_allowed_users_to_create_clients()
        context['description'] = 'Form for create a new client for your companies'
        return context

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            role = get_object_or_404(UserRole, name='client')
            user = form.save()
            assignation = UserToUserRole.objects.create(owner_id=request.POST['user'], user=user, role=role)
            messages.success(self.request, 'The client for user: "%s %s" has been added.' % (
                assignation.owner.first_name.title(), assignation.owner.last_name.title()
            ))
            return redirect('clients:user_clients')
        return super(ClientCreateView, self).get(self.request)

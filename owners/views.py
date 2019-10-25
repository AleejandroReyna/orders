from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import Group
from users.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from users.models import User


class UserOwnersListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'owners/owners_list.html'

    def get_queryset(self):
        return self.request.user.get_owners()


class OwnerCreateView(PermissionRequiredMixin, TemplateView):
    permission_required = 'users.add_user'
    template_name = 'owners/owner_form.html'

    def get_context_data(self, **kwargs):
        context = super(OwnerCreateView, self).get_context_data()
        context['form'] = UserCreationForm(self.request.POST or None)
        context['action'] = 'Create Owner'
        context['description'] = 'Form for create a new owner for his/her companies.'
        return context

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            group = get_object_or_404(Group, name='owner')
            user = form.save()
            user.groups.add(group)
            messages.success(self.request, "Owner for multiple companies has been added.")
            return redirect('dashboard:dashboard')

        messages.error(self.request, "Verify your data and try again")
        return super(OwnerCreateView, self).get(request)

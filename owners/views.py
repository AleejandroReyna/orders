from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from users.models import User


class UserOwnersListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'owners/owners_list.html'

    def get_queryset(self):
        return self.request.user.get_owners()

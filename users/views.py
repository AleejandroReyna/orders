from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin


class SearchUserView(PermissionRequiredMixin, TemplateView):
    permission_required = 'users.create_clients'
    template_name = 'users/search.html'

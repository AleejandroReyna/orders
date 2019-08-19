from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from companies import models
from django.contrib import messages


class CreateOfficeView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = models.Office
    template_name = 'offices/office_create_form.html'
    fields = ('name', 'company', 'phone', 'address')
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'companies.add_office'
    
    def form_valid(self, form):
        messages.success(self.request, 'Company has been added', extra_tags='success')
        return super(CreateOfficeView, self).form_valid(form)

    def get_success_url(self):
        return reverse('offices:office', kwargs={'office_id': self.object.pk})


class OfficeView(DetailView):
    pk_url_kwarg = 'office_id'
    model = models.Office
    template_name = 'offices/office_single.html'

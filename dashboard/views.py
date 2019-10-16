from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from companies import models as company_models


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data()
        context['companies'] = self.request.user.company_set.all()
        context['offices'] = company_models.Office.objects.filter(company__in=context['companies'])
        return context

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from exam_group import models


class ExamGroupCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.ExamGroup
    fields = ('name', 'description', 'category')
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_group.add_examgroup'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ExamGroupCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ExamGroupCreateView, self).get_context_data()
        context['action'] = 'Create'
        return context

    def get_success_url(self):
        return reverse_lazy('exam_group:exam_group', kwargs={'exam_group_id': self.object.pk})


class ExamGroupView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.ExamGroup
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_group.view_examgroup'
    pk_url_kwarg = 'exam_group_id'


class ExamGroupEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.ExamGroup
    fields = ('name', 'description')
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_group.change_examgroup'
    pk_url_kwarg = 'exam_group_id'

    def get_context_data(self, **kwargs):
        context = super(ExamGroupEditView, self).get_context_data()
        context['action'] = 'Edit'
        return context

    def get_success_url(self):
        return reverse_lazy('exam_group:exam_group', kwargs={'exam_group_id': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'The Exam Group with name: "%s" has been updated.' % form.instance.name)
        return super(ExamGroupEditView, self).form_valid(form)


class ExamGroupDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.ExamGroup
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_group.delete_examgroup'
    pk_url_kwarg = 'exam_group_id'
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(ExamGroupDeleteView, self).get_context_data()
        context['action'] = 'Delete'
        context['description'] = 'Are you sure to delete: "%s"?' % self.object.name
        return context


class ExamGroupListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.ExamGroup
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_group.view_examgroup'

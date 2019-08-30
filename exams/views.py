from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from exams import models


class ExamCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Exam
    fields = ('name', 'description', 'exam_group')
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.add_exam'

    def get_context_data(self, **kwargs):
        context = super(ExamCreateView, self).get_context_data()
        context['action'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'The exam with name: "%s" has been created.' % form.instance.name,
                         extra_tags='success')
        return super(ExamCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Verified your data and try again', extra_tags='danger')
        return super(ExamCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('exams:exam', kwargs={'exam_id': self.object.pk})


class ExamView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Exam
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.view_exam'
    pk_url_kwarg = 'exam_id'


class ExamEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Exam
    fields = ('name', 'description', 'exam_group')
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.change_exam'
    pk_url_kwarg = 'exam_id'
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(ExamEditView, self).get_context_data()
        context['action'] = 'Edit'
        return context

    def get_success_url(self):
        return reverse_lazy('exams:exam', kwargs={'exam_id': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'The exam with name: "%s" has been updated.' % form.instance.name,
                         extra_tags='success')
        return super(ExamEditView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Verified your data and try again', extra_tags='danger')
        return super(ExamEditView, self).form_invalid(form)


class ExamDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Exam
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.delete_exam'
    pk_url_kwarg = 'exam_id'
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(ExamDeleteView, self).get_context_data()
        context['action'] = 'Delete'
        context['description'] = 'Are you sure to delete the exam with name: "%s"?' % self.object.name
        return context

    def get_success_url(self):
        messages.success(self.request, 'The exam with name: "%s" has been deleted' % self.object.name, extra_tags='success')
        return reverse_lazy('exam_group:exam_group', kwargs={'exam_group_id': self.object.exam_group.pk})


class ExamListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Exam
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.view_exam'

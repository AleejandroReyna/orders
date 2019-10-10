from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from exams import models


class ExamCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Exam
    fields = ('name', 'description', 'category', 'type')
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
    fields = ('name', 'description', 'category', 'type')
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
        messages.success(self.request, 'The exam with name: "%s" has been deleted' % self.object.name,
                         extra_tags='success')
        return reverse_lazy('exam_group:exam_group', kwargs={'exam_group_id': self.object.exam_group.pk})


class ExamListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Exam
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.view_exam'


class ExamAssignStaticGroupView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Exam
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.change_exam'
    pk_url_kwarg = 'exam_id'
    template_name_suffix = '_assign_group_form'
    fields = ('response_type_group',)

    def get_context_data(self, **kwargs):
        context = super(ExamAssignStaticGroupView, self).get_context_data()
        context['action'] = 'Assign Response Group to'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Response group added for exam: "%s".' % self.object.name)
        return super(ExamAssignStaticGroupView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('exams:exam', kwargs={'exam_id': self.object.pk})


class ExamEditStaticGroupView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Exam
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.change_exam'
    pk_url_kwarg = 'exam_id'
    template_name_suffix = '_assign_group_form'
    fields = ('response_type_group',)

    def get_context_data(self, **kwargs):
        context = super(ExamEditStaticGroupView, self).get_context_data()
        context['action'] = 'Edit Response Group to'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Response group updated for exam: "%s".' % self.object.name)
        return super(ExamEditStaticGroupView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('exams:exam', kwargs={'exam_id': self.object.pk})


class ExamDynamicAssignationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.DynamicExamAssignation
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.add_dynamicexamassignation'
    fields = ('unit', 'min', 'max')

    def get_context_data(self, **kwargs):
        context = super(ExamDynamicAssignationCreateView, self).get_context_data()
        context['action'] = 'Create'
        context['exam'] = get_object_or_404(models.Exam, id=self.kwargs['exam_id'])
        return context

    def form_valid(self, form):
        exam = get_object_or_404(models.Exam, id=self.kwargs['exam_id'])
        assignation = form.save()
        exam.dynamic_exam_assignation = assignation
        exam.save()
        messages.success(self.request, 'Dynamic assignation for exam: "%s" with min: %s and max: %s created.' %
                         (exam.name, assignation.min, assignation.max))
        return redirect('exams:exam', exam_id=exam.pk)


class ExamDynamicAssignationEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.DynamicExamAssignation
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.change_dynamicexamassignation'
    fields = ('unit', 'min', 'max')
    pk_url_kwarg = 'dynamic_exam_assignation_id'

    def get_context_data(self, **kwargs):
        context = super(ExamDynamicAssignationEditView, self).get_context_data()
        context['action'] = 'Edit'
        context['exam'] = self.object.exam
        return context

    def get_success_url(self):
        messages.success(self.request, 'Exam Assignation for exam: "%s" has been updated.' %
                         self.object.exam.name.capitalize())
        return reverse_lazy('exams:exam', kwargs={'exam_id': self.object.exam.pk})


class ExamDynamicAssignationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.DynamicExamAssignation
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exams.delete_dynamicexamassignation'
    pk_url_kwarg = 'dynamic_exam_assignation_id'

    def get_context_data(self, **kwargs):
        context = super(ExamDynamicAssignationDeleteView, self).get_context_data()
        context['action'] = 'Delete'
        context['description'] = 'Are you sure to delete this assignation?'
        return context

    def get_success_url(self):
        messages.success(self.request, 'The assignation for exam: "%s" has been deleted.' %
                         self.object.exam.name.title())
        return reverse_lazy('exams:exam', kwargs={'exam_id': self.object.exam.pk})

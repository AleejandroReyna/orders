from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from exam_response_types import models
from django.urls import reverse_lazy
from django.contrib import messages


class ResponseTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.ResponseType
    fields = ('name', 'description')
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.add_responsetype'

    def get_success_url(self):
        return reverse_lazy('exam_response_types:response_type', kwargs={'response_type_id': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ResponseTypeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ResponseTypeCreateView, self).get_context_data()
        context['action'] = 'Create'
        return context


class ResponseTypeEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.ResponseType
    fields = ('name', 'description')
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    pk_url_kwarg = 'response_type_id'
    permission_required = 'exam_response_types.change_responsetype'

    def get_success_url(self):
        messages.success(self.request, 'The response type with name: "%s" has been added.' % self.object.name,
                         extra_tags='success')
        return reverse_lazy('exam_response_types:response_type', kwargs={'response_type_id': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ResponseTypeEditView, self).get_context_data()
        context['action'] = 'Edit'
        return context


class ResponseTypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.ResponseType
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    pk_url_kwarg = 'response_type_id'
    permission_required = 'exam_response_types.delete_responsetype'
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(ResponseTypeDeleteView, self).get_context_data()
        context['action'] = 'Delete'
        context['description'] = 'Are you sure to delete response type with name: "%s"?' % self.object.name
        return context

    def get_success_url(self):
        messages.success(self.request, 'Response type with name: "%s" has been deleted' % self.object.name)
        return reverse_lazy('exam_response_types:response_types')


class ResponseTypeView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.ResponseType
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.view_responsetype'
    pk_url_kwarg = 'response_type_id'


class ResponseTypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.ResponseType
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.view_responsetype'


''' GROUPS '''


class ResponseTypeGroupCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.ResponseTypeGroup
    fields = ('name', 'description')
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.add_responsetypegroup'

    def get_context_data(self, **kwargs):
        context = super(ResponseTypeGroupCreateView, self).get_context_data()
        context['action'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'The group with name: "%s" has been added' % form.instance.name,
                         extra_tags='success')
        return super(ResponseTypeGroupCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('exam_response_types_groups:response_type_group',
                            kwargs={'response_type_group_id': self.object.pk})


class ResponseTypeGroupView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.ResponseTypeGroup
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.view_responsetypegroup'
    pk_url_kwarg = 'response_type_group_id'


class ResponseTypeGroupListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.ResponseTypeGroup
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.view_responsetypegroup'


class ResponseTypeGroupEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.ResponseTypeGroup
    fields = ('name', 'description')
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.add_responsetypegroup'
    pk_url_kwarg = 'response_type_group_id'

    def get_context_data(self, **kwargs):
        context = super(ResponseTypeGroupEditView, self).get_context_data()
        context['action'] = 'Edit'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'The group with name: "%s" has been updated.' % form.instance.name,
                         extra_tags='success')
        return super(ResponseTypeGroupEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('exam_response_types_groups:response_type_group',
                            kwargs={'response_type_group_id': self.object.pk})


''' ASSIGNATIONS '''


class ResponseTypeAssignationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.ResponseTypeAssignation
    fields = ('response_type', 'weighing')
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.add_responsetypeassignation'

    def get_context_data(self, **kwargs):
        context = super(ResponseTypeAssignationCreateView, self).get_context_data()
        context['group'] = get_object_or_404(models.ResponseTypeGroup, id=self.kwargs['response_type_group_id'])
        context['form'].fields['response_type'].queryset = models.ResponseType.objects\
            .exclude(id__in=[item.pk for item in context['group'].response_types.all()])
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.user = self.request.user
        form.instance.response_type_group = context['group']
        messages.success(self.request,
                         'The assignation of response type: "%s" for group: "%s" with value: "%s" has been added' % (
                             form.instance.response_type.name, form.instance.response_type_group.name,
                             form.instance.weighing
                         ))
        return super(ResponseTypeAssignationCreateView, self).form_valid(form)

    def get_success_url(self):
        context = self.get_context_data()
        return reverse_lazy('exam_response_types_groups:response_type_group',
                            kwargs={'response_type_group_id': context['group'].pk})


class ResponseTypeAssignationEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.ResponseTypeAssignation
    pk_url_kwarg = 'response_type_assignation_id'
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.change_responsetypeassignation'
    template_name_suffix = '_edit_form'
    fields = ('weighing',)

    def get_context_data(self, **kwargs):
        context = super(ResponseTypeAssignationEditView, self).get_context_data()
        context['action'] = 'Edit'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'The assignation for group: "%s" with response type: "%s" has been updated.' % (
            self.object.response_type_group.name.title(), self.object.response_type.name.title()
        ))
        return super(ResponseTypeAssignationEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('exam_response_types_groups:response_type_group',
                            kwargs={'response_type_group_id': self.object.response_type_group.pk})


class ResponseTypeAssignationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.ResponseTypeAssignation
    pk_url_kwarg = 'response_type_assignation_id'
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.delete_responsetypeassignation'
    template_name_suffix = '_delete_form'

    def get_context_data(self, **kwargs):
        context = super(ResponseTypeAssignationDeleteView, self).get_context_data()
        context['action'] = 'Delete'
        context['description'] = 'Are you sure to delete the assignation for group: "%s" with response type: "%s" ' \
                                 'and value: "%s"?' % (self.object.response_type_group.name.title(),
                                                       self.object.response_type.name.title(),
                                                       self.object.weighing)
        return context

    def get_success_url(self):
        messages.success(self.request, 'The assignation for group: "%s" has been deleted.' %
                         self.object.response_type_group.name.title())
        return reverse_lazy('exam_response_types_groups:response_type_group',
                            kwargs={'response_type_group_id': self.object.response_type_group.pk})


''' UNITS '''


class UnitCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Unit
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    fields = ('name', 'description')
    permission_required = 'exam_response_types.add_unit'

    def get_context_data(self, **kwargs):
        context = super(UnitCreateView, self).get_context_data()
        context['action'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.name = form.instance.name.lower()
        form.instance.user = self.request.user
        count = models.Unit.objects.filter(name=form.instance.name.lower()).count()
        if count == 0:
            return super(UnitCreateView, self).form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Verified if name is unique.', extra_tags='danger')
        return super(UnitCreateView, self).form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Unit with name: "%s" has been added.' % self.object.name)
        return reverse_lazy('units:unit', kwargs={'unit_id': self.object.pk})


class UnitEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Unit
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    fields = ('name', 'description')
    permission_required = 'exam_response_types.change_unit'
    pk_url_kwarg = 'unit_id'
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(UnitEditView, self).get_context_data()
        context['action'] = 'Edit'
        return context

    def form_valid(self, form):
        form.instance.name = form.instance.name.lower()
        count = models.Unit.objects.filter(name=form.instance.name.lower()).count()
        print(count)
        if count == 1 or count == 0:
            return super(UnitEditView, self).form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Verified if name is unique.', extra_tags='danger')
        return super(UnitEditView, self).form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Unit with name: "%s" has been updated.' % self.object.name)
        return reverse_lazy('units:unit', kwargs={'unit_id': self.object.pk})


class UnitDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Unit
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.change_unit'
    pk_url_kwarg = 'unit_id'
    template_name_suffix = '_form'

    def get_success_url(self):
        messages.success(self.request, 'The unit with name: "%s" has been deleted' % self.object.name)
        return reverse_lazy('units:unit_list')

    def get_context_data(self, **kwargs):
        context = super(UnitDeleteView, self).get_context_data()
        context['action'] = 'Delete'
        context['description'] = 'Are you sure to delete Unit with name: "%s"?' % self.object.name
        return context


class UnitView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Unit
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.view_unit'
    pk_url_kwarg = 'unit_id'


class UnitListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Unit
    login_url = reverse_lazy('custom_auth:login')
    redirect_field_name = 'redirect_to'
    permission_required = 'exam_response_types.view_unit'

from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from categories import models
from django.urls import reverse_lazy
from django.contrib import messages


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Category
    fields = ('name', 'description')
    redirect_field_name = 'redirect_to'
    login_url = '/auth/login'
    permission_required = 'categories.add_category'

    def get_success_url(self):
        return reverse_lazy('categories:category', kwargs={'category_id': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,
                         'Category with name: %s has been added.' % form.cleaned_data['name'], extra_tags='success')
        return super(CategoryCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data()
        context['action'] = 'Create'
        context['description'] = 'Create a category for multiple exams.'
        return context


class CategoryView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Category
    pk_url_kwarg = 'category_id'
    template_name_suffix = '_detail'
    login_url = '/auth/login'
    permission_required = 'categories.view_category'


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Category
    template_name_suffix = '_list'
    login_url = '/auth/login'
    permission_required = 'categories.view_category'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['description'] = 'View all categories.'
        return context


class CategoryEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Category
    pk_url_kwarg = 'category_id'
    template_name_suffix = '_form'
    login_url = '/auth/login'
    permission_required = 'categories.change_category'
    fields = ('name', 'description')

    def get_context_data(self, **kwargs):
        context = super(CategoryEditView, self).get_context_data()
        context['action'] = 'Edit'
        return context

    def get_success_url(self):
        return reverse_lazy('categories:category', kwargs={'category_id': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Category with name: %s has been updated.' % form.instance.name,
                         extra_tags='success')
        return super(CategoryEditView, self).form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Category
    pk_url_kwarg = 'category_id'
    template_name_suffix = '_form'
    login_url = '/auth/login'
    permission_required = 'categories.delete_category'
    success_url = reverse_lazy('categories:categories')

    def get_context_data(self, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data()
        context['action'] = 'Delete'
        context['description'] = 'Are you sure to delete category with name: "%s"?' % self.object.name
        return context

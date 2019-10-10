from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import views, mixins, models as userModels
from django.contrib import messages
from collaborators import models
from django.urls import reverse_lazy
from django.shortcuts import redirect


class UserCreateView(mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, CreateView):
    model = userModels.User
    fields = ('first_name', 'last_name', 'email')
    template_name = 'collaborators/collaborator_form.html'
    login_url = '/auth/login'
    redirect_field_name = 'redirect_to'
    permission_required = 'auth.add_user'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        context['action'] = 'Create'
        context['description'] = 'Create a collaborator for your companies.'
        return context

    def form_valid(self, form):
        username = "%s_%s" % (
            form['first_name'].value().replace(" ", "_").lower(),
            form['last_name'].value().replace(" ", "_").lower())
        possibles = userModels.User.objects.filter(username__contains=username).count()
        password = "%s%s123!#" % (form['first_name'].value().title().replace(" ", ""),
                                  form['last_name'].value().title().replace(" ", ""))
        if possibles > 0:
            username = "%s_%s" % (username, possibles)
        form.instance.username = username
        form.instance.password = password
        new_user = form.save()
        new_user.set_password(password)
        new_user.save()
        new_vinculation = models.UserCollaborator.objects.create(collaborator=new_user, administrator=self.request.user)
        messages.success(self.request, 'User with username: %s has been added.')
        return redirect('dashboard:dashboard')

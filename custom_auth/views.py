from django.shortcuts import render
from users.forms import AuthenticationForm
from django.views.generic import TemplateView, View
from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import redirect
from django.contrib import messages


class LoginView(TemplateView):
    template_name = 'auth/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data()
        context['form'] = AuthenticationForm()
        print(context['form'])
        return context

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            try:
                route = request.POST['redirect_to']
                return redirect(route)
            except Exception as e:
                print(e)
                pass
            return redirect('dashboard:dashboard')

        messages.error(request, "Invalid credentials.")
        return redirect('custom_auth:login')


class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'Logout successfully')
        return redirect('pages:home')

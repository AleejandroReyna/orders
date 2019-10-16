from django.contrib.auth.forms import \
    UserCreationForm as BaseUserCreationForm, \
    UserChangeForm as BaseUserChangeForm, \
    AuthenticationForm as BaseAuthenticationForm
from users.models import User


class AuthenticationForm(BaseAuthenticationForm):

    class Meta(BaseAuthenticationForm):
        model = User
        fields = ('email', 'password')

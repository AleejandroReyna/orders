from django.contrib.auth.forms import \
    UserCreationForm as BaseUserCreationForm, \
    UserChangeForm as BaseUserChangeForm, \
    AuthenticationForm as BaseAuthenticationForm
from users.models import User


class AuthenticationForm(BaseAuthenticationForm):

    class Meta(BaseAuthenticationForm):
        model = User
        fields = ('email', 'password')


class UserCreationForm(BaseUserCreationForm):

    class Meta(BaseUserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserChangeForm(BaseUserChangeForm):

    class Meta(BaseUserChangeForm):
        model = User
        fields = ('first_name', 'last_name', 'email')

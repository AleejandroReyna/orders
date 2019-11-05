from users.forms import UserCreationForm
from users.models import User
from django import forms


class CreateClientForm(UserCreationForm):
    user = forms.ModelChoiceField(User.get_superuser_owners_method())

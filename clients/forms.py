from django import forms
from companies.models import Company
from django.contrib.auth.models import User


class CreateClientForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    company = forms.ModelChoiceField(queryset=Company.objects.all())


class ClientForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

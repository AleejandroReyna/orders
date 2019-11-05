from  companies.models import Company
from users.models import User
from django import forms


class CreateCompanyForm(forms.ModelForm):
    user = forms.ChoiceField(choices=[(user.pk, "%s %s (%s)" % (user.first_name.title(),
                                                                user.last_name.title(),
                                                                user.email)
                                       ) for user in User.get_superuser_owners_method()])

    class Meta:
        model = Company
        fields = ('name', 'address', 'phone', 'description', 'nit')

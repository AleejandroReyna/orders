from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import CustomUserManager
from companies import models as company_models
from django.utils import timezone
from django.db import models


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = None
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()
        return super(User, self).save(*args, **kwargs)

    def get_collaborators(self):
        return User.objects.filter(user__owner_id=self.pk, user__role__name='collaborator')\
            .order_by('-user__created_at')

    def get_clients(self):
        return User.objects.filter(user__owner_id=self.pk, user__role__name='client')

    def get_owners(self):
        return User.objects.filter(owner__user_id=self.pk, owner__role__name='collaborator')

    def get_companies(self):
        return company_models.Company.objects.filter(companyuserrole__user=self,
                                                     companyuserrole__company_role__name='administrator')

    class Meta:
        permissions = [
            ("create_collaborators", "Create collaborator for company"),
            ("view_collaborators", "View collaborators for company"),
            ("create_clients", "Create client for company"),
            ("view_clients", "View clients for company"),
            ("view_owners", "View owners for collaborators")
        ]


class UserRole(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(UserRole, self).save(*args, **kwargs)


class UserToUserRole(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

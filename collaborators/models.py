from django.db import models
from django.contrib.auth.models import User


class UserCollaborator(models.Model):
    administrator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collaborator')
    collaborator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='administrator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s_%s_%s" % (self.administrator.pk, self.collaborator.pk, self.created_at)

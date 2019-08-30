from django.db import models
from django.contrib.auth.models import User


class ResponseType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name


class ResponseTypeGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name


WEIGHING_CHOICES = (('normal', 'Normal'), ('warning', 'Warning'), ('danger', 'Danger'))


class ResponseTypeAssignation(models.Model):
    response_type = models.ForeignKey(ResponseType, on_delete=models.CASCADE)
    response_type_group = models.ForeignKey(ResponseTypeGroup, on_delete=models.CASCADE)
    weighing = models.CharField(max_length=20, choices=WEIGHING_CHOICES, default='normal')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s__%s__%s" % ( self.response_type.pk, self.response_type_group.pk, self.weighing )

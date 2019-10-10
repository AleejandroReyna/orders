from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from exam_response_types.models import ResponseTypeGroup, Unit

TYPE_CHOICES = (('static', 'static'), ('dynamic', 'dynamic'))


class Parameter(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=20, null=True, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name


class DynamicParameterAssignation(models.Model):
    parameter = models.OneToOneField(Parameter, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    min = models.FloatField(default=0)
    max = models.FloatField(default=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s__%s__%s__%s" % (self.pk, self.unit.name, self.min, self.max)


class StaticParameterAssignation(models.Model):
    parameter = models.OneToOneField(Parameter, on_delete=models.CASCADE)
    response_type_group = models.ForeignKey(ResponseTypeGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s__%s" % (self.parameter.pk, self.response_type_group.pk)

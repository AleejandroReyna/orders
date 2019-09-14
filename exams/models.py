from django.db import models
from exam_group.models import ExamGroup
from django.contrib.auth.models import User
from exam_response_types.models import ResponseTypeGroup, Unit

TYPE_CHOICES = (('static', 'static'), ('dynamic', 'dynamic'))


class DynamicExamAssignation(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    min = models.FloatField(default=0)
    max = models.FloatField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s__%s__%s__%s" % (self.pk, self.unit.name, self.min, self.max)


class Exam(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    exam_group = models.ForeignKey(ExamGroup, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=20, null=True, choices=TYPE_CHOICES)
    response_type_group = models.ForeignKey(ResponseTypeGroup, on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
    dynamic_exam_assignation = models.OneToOneField(DynamicExamAssignation, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

from django.db import models
from exam_group.models import ExamGroup
from django.contrib.auth.models import User


class Exam(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    exam_group = models.ForeignKey(ExamGroup, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

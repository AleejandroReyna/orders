from django.db import models
from categories.models import Category
from django.contrib.auth.models import User


class ExamGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

from django.db import models
from django.contrib.auth.models import User


class AnalysisRole(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name.title()

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(AnalysisRole, self).save()


class Analysis(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, through="AnalysisUserRole")
    roles = models.ManyToManyField(AnalysisRole, through="AnalysisUserRole")

    def __str__(self):
        return "%s" % self.name.title()

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Analysis, self).save()


class AnalysisUserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    role = models.ForeignKey(AnalysisRole, on_delete=models.CASCADE)

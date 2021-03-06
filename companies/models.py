from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from crequest.middleware import CrequestMiddleware
from exams.models import Exam, TYPE_CHOICES
from exam_response_types.models import Unit, ResponseTypeGroup


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True)
    phone = PhoneNumberField(null=True)
    description = models.TextField(null=True)
    nit = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, through='CompanyUserRole')
    exams = models.ManyToManyField(Exam, through='CompanyExamAssociation')

    def __str__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        current_request = CrequestMiddleware.get_request()
        super(Company, self).save(*args, **kwargs)
        offices = self.office_set.count()
        if offices == 0:
            current_user = current_request.user
            central = self.office_set.create(name='central')
            self.companyuserrole_set.create(user=current_user, company_role_id=1)


class Office(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=True)
    address = models.TextField(null=True)
    users = models.ManyToManyField(User, through='OfficeUserRole')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name


class CompanyRole(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name


class CompanyUserRole(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_role = models.ForeignKey(CompanyRole, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s_%s_%s" % (self.company.pk, self.user.pk, self.company_role.pk)


class OfficeUserRole(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_role = models.ForeignKey(CompanyRole, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s_%s_%s" % (self.office.pk, self.user.pk, self.company_role.pk)


class CompanyExamAssociation(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    exam = models.ForeignKey(Exam, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CompanyExamAssociationValue(models.Model):
    company_exam_association = models.OneToOneField(CompanyExamAssociation, on_delete=models.CASCADE)
    response_type_group = models.ForeignKey(ResponseTypeGroup, on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    min = models.FloatField(null=True)
    max = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from clients import forms
from companies.models import Company, CompanyRole, CompanyUserRole
from django.shortcuts import redirect
from django.contrib import messages

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import views, mixins, models as userModels
from django.contrib import messages
from collaborators import models
from django.urls import reverse_lazy
from django.shortcuts import redirect

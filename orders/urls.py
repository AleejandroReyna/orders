"""orders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('response_type_assignations/', include('parameters_response_types.assignations_urls')),
    path('response_type_groups/', include('parameters_response_types.groups_urls')),
    path('exam_dynamic_assignations/', include('exams.assignations_urls')),
    path('response_types/', include('parameters_response_types.urls')),
    path('units/', include('parameters_response_types.units_urls')),
    path('company_exams/', include('companies.company_exams_urls')),
    path('parameters/', include('analysis_parameters.urls')),
    path('collaborators/', include('collaborators.urls')),
    path('categories/', include('categories.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('companies/', include('companies.urls')),
    path('analysis/', include('analysis.urls')),
    path('auth/', include('custom_auth.urls')),
    path('offices/', include('offices.urls')),
    path('clients/', include('clients.urls')),
    path('owners/', include('owners.urls')),
    path('exams/', include('exams.urls')),
    path('users/', include('users.urls'))
]

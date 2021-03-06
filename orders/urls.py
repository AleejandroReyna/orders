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
    path('auth/', include('custom_auth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('companies/', include('companies.urls')),
    path('offices/', include('offices.urls')),
    path('collaborators/', include('collaborators.urls')),
    path('clients/', include('clients.urls')),
    path('categories/', include('categories.urls')),
    path('exam_groups/', include('exam_group.urls')),
    path('exams/', include('exams.urls')),
    path('response_types/', include('exam_response_types.urls')),
    path('response_type_groups/', include('exam_response_types.groups_urls')),
    path('response_type_assignations/', include('exam_response_types.assignations_urls')),
    path('units/', include('exam_response_types.units_urls')),
    path('exam_dynamic_assignations/', include('exams.assignations_urls')),
    path('company_exams/', include('companies.company_exams_urls'))
]

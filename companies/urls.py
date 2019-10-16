from django.urls import path
from companies import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='list_company'),
    path('new/', views.CompanyCreateView.as_view(), name='new_company'),
    path('<int:company_id>/', views.CompanyView.as_view(), name='company'),
    path('<int:company_id>/edit/', views.CompanyEditView.as_view(), name='edit_company'),
    path('<int:company_id>/delete/', views.CompanyDeleteView.as_view(), name='delete_company'),
    path('<int:company_id>/new_office/', views.CreateCompanyOfficeView.as_view(), name='new_office')
]

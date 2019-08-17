from django.urls import path
from companies import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='list_company'),
    path('<int:company_id>/', views.CompanyView.as_view(), name='company'),
    path('new/', views.CreateCompanyView.as_view(), name='new_company')
]

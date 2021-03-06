from django.urls import path
from companies import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='list_company'),
    path('new/', views.CompanyCreateView.as_view(), name='new_company'),
    path('<int:company_id>/', views.CompanyView.as_view(), name='company'),
    path('<int:company_id>/edit/', views.CompanyEditView.as_view(), name='edit_company'),
    path('<int:company_id>/delete/', views.CompanyDeleteView.as_view(), name='delete_company'),
    path('<int:company_id>/new_office/', views.CreateCompanyOfficeView.as_view(), name='new_office'),
    path('<int:company_id>/exams/', views.CompanyExamsListView.as_view(), name='list_company_exams'),
    path('<int:company_id>/add_exam_association/', views.CreateCompanyExamAssociationView.as_view(),
         name='create_exam_association'),
    path('<int:exam_association_id>/add_type/', views.CreateCompanyExamAssociationValueView.as_view(),
         name='create_exam_association_value')
]

from django.urls import path
from companies.views import EditCompanyExamAssociationValueTypeStaticView, \
    EditCompanyExamAssociationValueTypeDynamicView, EditCompanyExamAssociationValueView

app_name = 'company_exams'

urlpatterns = [
    path('<int:exam_association_value_id>/edit_static_values/', EditCompanyExamAssociationValueTypeStaticView.as_view(),
         name='update_exam_association_value_static'),
    path('<int:exam_association_value_id>/edit_dynamic_values/',
         EditCompanyExamAssociationValueTypeDynamicView.as_view(), name='update_exam_association_value_dynamic'),
    path('<int:exam_association_value_id>/edit/', EditCompanyExamAssociationValueView.as_view(),
         name='update_exam_association_value'),

]

from django.urls import path
from parameters_response_types.views import ResponseTypeAssignationEditView, ResponseTypeAssignationDeleteView

app_name = 'exam_response_types_assignations'

urlpatterns = [
    path('<int:response_type_assignation_id>/edit/', ResponseTypeAssignationEditView.as_view(),
         name='edit_response_type_assignation'),
    path('<int:response_type_assignation_id>/delete/', ResponseTypeAssignationDeleteView.as_view(),
         name='delete_response_type_assignation')
]

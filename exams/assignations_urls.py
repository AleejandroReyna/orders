from django.urls import path
from exams.views import ExamDynamicAssignationEditView, ExamDynamicAssignationDeleteView

app_name = 'exam_dynamic_assignations'

urlpatterns = [
    path('<int:dynamic_exam_assignation_id>/edit/', ExamDynamicAssignationEditView.as_view(), name='edit_assignation'),
    path('<int:dynamic_exam_assignation_id>/delete/', ExamDynamicAssignationDeleteView.as_view(),
         name='delete_assignation')
]

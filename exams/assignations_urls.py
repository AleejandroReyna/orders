from django.urls import path
from exams.views import ExamDynamicAssignationEditView

app_name = 'exam_dynamic_assignations'

urlpatterns = [
    path('<int:dynamic_exam_assignation_id>/edit/', ExamDynamicAssignationEditView.as_view(), name='edit_assignation')
]

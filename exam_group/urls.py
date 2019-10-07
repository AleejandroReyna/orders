from django.urls import path
from exam_group import views

app_name = 'exam_group'

urlpatterns = [
    path('', views.ExamGroupListView.as_view(), name='list_exam_group'),
    path('new/', views.ExamGroupCreateView.as_view(), name='new_exam_group'),
    path('<int:exam_group_id>/', views.ExamGroupView.as_view(), name='exam_group'),
    path('<int:exam_group_id>/edit/', views.ExamGroupEditView.as_view(), name='edit_exam_group'),
    path('<int:exam_group_id>/delete/', views.ExamGroupDeleteView.as_view(), name='delete_exam_group')
]

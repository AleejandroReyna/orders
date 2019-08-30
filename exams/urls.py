from django.urls import path
from exams import views

app_name = 'exams'

urlpatterns = [
    path('', views.ExamListView.as_view(), name='list_exams'),
    path('new/', views.ExamCreateView.as_view(), name='new_exam'),
    path('<int:exam_id>/', views.ExamView.as_view(), name='exam'),
    path('<int:exam_id>/edit/', views.ExamEditView.as_view(), name='edit_exam'),
    path('<int:exam_id>/delete/', views.ExamDeleteView.as_view(), name='delete_exam')
]

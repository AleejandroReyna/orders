from django.urls import path
from analysis import views

app_name = 'analysis'

urlpatterns = [
    path('', views.AnalysisListView.as_view(), name='analysis_list'),
    path('new/', views.AnalysisCreateView.as_view(), name='create_analysis'),
    path('<int:analysis_id>/', views.AnalysisView.as_view(), name='analysis'),
    path('<int:analysis_id>/edit/', views.AnalysisEditView.as_view(), name='edit_analysis'),
    path('<int:analysis_id>/delete/', views.AnalysisDeleteView.as_view(), name='delete_analysis')
]

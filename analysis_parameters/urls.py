from django.urls import path
from analysis_parameters import views

app_name = 'parameters'

urlpatterns = [
    path('', views.ParameterListView.as_view(), name='parameters'),
    path('new/', views.ParameterCreateView.as_view(), name='create_parameter'),
    path('<int:parameter_id>/', views.ParameterView.as_view(), name='parameter'),
    path('<int:parameter_id>/edit/', views.ParameterEditView.as_view(), name='edit_parameter'),
    path('<int:parameter_id>/delete/', views.ParameterDeleteView.as_view(), name='delete_parameter')
]

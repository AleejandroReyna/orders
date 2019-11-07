from django.urls import path
from parameters_response_types.views import ResponseTypeCreateView, ResponseTypeView, ResponseTypeListView, \
    ResponseTypeEditView, ResponseTypeDeleteView

app_name = 'parameters_response_types'

urlpatterns = [
    path('', ResponseTypeListView.as_view(), name='response_types'),
    path('new/', ResponseTypeCreateView.as_view(), name='new_response_type'),
    path('<int:response_type_id>/', ResponseTypeView.as_view(), name='response_type'),
    path('<int:response_type_id>/edit/', ResponseTypeEditView.as_view(), name='edit_response_type'),
    path('<int:response_type_id>/delete/', ResponseTypeDeleteView.as_view(), name='delete_response_type')
]
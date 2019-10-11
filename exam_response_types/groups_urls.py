from django.urls import path
from exam_response_types.views import ResponseTypeGroupCreateView, ResponseTypeGroupView,\
    ResponseTypeAssignationCreateView, ResponseTypeGroupListView, ResponseTypeGroupEditView, \
    ResponseTypeGroupDeleteView

app_name = 'exam_response_types_groups'

urlpatterns = [
    path('', ResponseTypeGroupListView.as_view(), name='response_type_groups'),
    path('new/', ResponseTypeGroupCreateView.as_view(), name='new_response_type_group'),
    path('<int:response_type_group_id>/', ResponseTypeGroupView.as_view(), name='response_type_group'),
    path('<int:response_type_group_id>/edit/', ResponseTypeGroupEditView.as_view(), name='edit_response_type_group'),
    path('<int:response_type_group_id>/delete/', ResponseTypeGroupDeleteView.as_view(),
         name='delete_response_type_group'),
    path('<int:response_type_group_id>/add_response_type/', ResponseTypeAssignationCreateView.as_view(),
         name='assign_response_type_to_group')
]

from django.urls import path
from exam_response_types.views import ResponseTypeCreateView, ResponseTypeView, ResponseTypeListView

app_name = 'exam_response_types'

urlpatterns = [
    path('', ResponseTypeListView.as_view(), name='response_types'),
    path('new/', ResponseTypeCreateView.as_view(), name='new_response_type'),
    path('<int:response_type_id>/', ResponseTypeView.as_view(), name='response_type')
]
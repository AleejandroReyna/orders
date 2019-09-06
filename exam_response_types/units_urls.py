from django.urls import path
from exam_response_types.views import UnitCreateView, UnitView

app_name = 'units'

urlpatterns = [
    path('new/', UnitCreateView.as_view(), name='new_unit'),
    path('<int:unit_id>/', UnitView.as_view(), name='unit')
]

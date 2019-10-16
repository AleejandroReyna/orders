from django.urls import path
from parameters_response_types.views import UnitCreateView, UnitView, UnitListView, UnitEditView, UnitDeleteView

app_name = 'units'

urlpatterns = [
    path('', UnitListView.as_view(), name='unit_list'),
    path('new/', UnitCreateView.as_view(), name='new_unit'),
    path('<int:unit_id>/', UnitView.as_view(), name='unit'),
    path('<int:unit_id>/edit/', UnitEditView.as_view(), name='edit_unit'),
    path('<int:unit_id>/delete/', UnitDeleteView.as_view(), name='delete_unit')
]

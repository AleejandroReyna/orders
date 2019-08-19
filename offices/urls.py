from django.urls import path
from offices import views

app_name = 'offices'

urlpatterns = [
    path('new/', views.OfficeCreateView.as_view(), name='new_office'),
    path('<int:office_id>/', views.OfficeView.as_view(), name='office'),
    path('<int:office_id>/edit/', views.OfficeEditView.as_view(), name='edit_office'),
    path('<int:office_id>/delete/', views.OfficeDeleteView.as_view(), name='delete_office')
]

from django.urls import path
from offices import views

app_name = 'offices'

urlpatterns = [
    path('new/', views.CreateOfficeView.as_view(), name='new_office'),
    path('<int:office_id>/', views.OfficeView.as_view(), name='office')
]

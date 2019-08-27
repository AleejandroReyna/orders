from django.urls import path
from clients import views

app_name = 'clients'

urlpatterns = [
    path('new/', views.CreateCompanyClientView.as_view(), name='create_client')
]

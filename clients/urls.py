from django.urls import path
from clients import views

app_name = 'clients'

urlpatterns = [
    path('my_clients/', views.UserClientsListView.as_view(), name='user_clients'),
    path('new/', views.ClientCreateView.as_view(), name='create_client')
]

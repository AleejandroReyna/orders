from django.urls import path
from owners import views

app_name = 'owners'

urlpatterns = [
    path('new/', views.OwnerCreateView.as_view(), name='create_owner'),
    path('my_owners/', views.UserOwnersListView.as_view(), name='user_owners')
]

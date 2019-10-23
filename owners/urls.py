from django.urls import path
from owners import views

app_name = 'owners'

urlpatterns = [
    path('my_owners/', views.UserOwnersListView.as_view(), name="user_owners")
]

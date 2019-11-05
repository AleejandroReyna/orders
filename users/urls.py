from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('search/', views.SearchUserView.as_view(), name='search')
]
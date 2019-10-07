from django.urls import path
from collaborators import views

app_name = 'collaborators'

urlpatterns = [
    path('new/', views.UserCreateView.as_view(), name='new_collaborator')
]

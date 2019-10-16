from django.urls import path
from collaborators import views

app_name = 'collaborators'

urlpatterns = [
    path('new/', views.CollaboratorCreateView.as_view(), name='create_collaborator')
]

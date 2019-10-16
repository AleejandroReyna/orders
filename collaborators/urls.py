from django.urls import path
from collaborators import views

app_name = 'collaborators'

urlpatterns = [
    path('my_collaborators/', views.UserCollaboratorsListView.as_view(), name='user_collaborators'),
    path('new/', views.CollaboratorCreateView.as_view(), name='create_collaborator')
]

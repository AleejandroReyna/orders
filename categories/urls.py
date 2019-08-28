from django.urls import path
from categories import views

app_name = 'categories'

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='categories'),
    path('new/', views.CategoryCreateView.as_view(), name='new_category'),
    path('<int:category_id>/', views.CategoryView.as_view(), name='category'),
    path('<int:category_id>/edit/', views.CategoryEditView.as_view(), name='edit_category'),
    path('<int:category_id>/delete/', views.CategoryDeleteView.as_view(), name='delete_category')
]

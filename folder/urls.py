from django.urls import path
from . import views

app_name = 'folder'

urlpatterns = [
    path('add/', views.FolderCreateView.as_view(), name='add'),
    path('', views.FolderListView.as_view(), name='list'),
]

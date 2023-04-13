from django.urls import path
from . import views

app_name = 'file'


urlpatterns = [
    path('add/', views.FileCreateView.as_view(), name='add'),
    path('list/', views.FileListView.as_view(), name='list'),
    path('<int:pk>/download/', views.FileDownloadView.as_view(), name='download'),
]

from django.urls import path
from .views import CSVUploadView, StudentListView

urlpatterns = [
    path('upload/', CSVUploadView.as_view(), name='csv-upload'),
    path('students/', StudentListView.as_view(), name='student-list'),
]


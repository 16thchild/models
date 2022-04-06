from django.urls import path
from . import views


urlpatterns = [
    path('', views.test_view, name='test'),
    #path('', views.TestAPI.as_view(), name='test'),
    path('upload-url/', views.GetUploadURL.as_view(), name='upload_url'),
    path('download-url/', views.GetDownloadURL.as_view(), name='download_url'),
]
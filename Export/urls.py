from django.urls import path

from Export.views import ExportAPIView

base_url = 'v1'

urlpatterns = [
    path('', ExportAPIView.as_view())
]

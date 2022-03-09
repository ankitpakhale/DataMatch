from django.urls import path
from .views import *

urlpatterns = [
    
    path('index/', index,name='INDEX'),
    path('', UploadCSVView.as_view(),name='UPLOAD')
]
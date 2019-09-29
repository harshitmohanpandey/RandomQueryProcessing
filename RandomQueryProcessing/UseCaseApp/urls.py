from django.conf.urls import url
from UseCaseApp import views

urlpatterns = [
    url(r'^(?i)usecase/', views.check.as_view()), 
]
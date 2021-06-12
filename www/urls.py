from django.urls import path
from . import views


app_name  = 'www'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('participate', views.CandidatePageView.as_view(), name='candidate'),
]
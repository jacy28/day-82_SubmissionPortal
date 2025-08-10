from django.urls import path
from . import views

urlpatterns=[
    path('', views.resume_submit, name='resume_submit'),
    path('resumes', views.resume_list, name='resume_list'),
]
from django.urls import path
from .views import ResumesView
from vacancy.views import LoggedUserHomePageView

urlpatterns = [
    path('resumes', ResumesView.as_view(), name="resumes"),
    path('resume/new', LoggedUserHomePageView.as_view(), name='resume_new'),

]
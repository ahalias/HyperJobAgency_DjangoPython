from django.urls import path
from .views import MainPageView, VacanciesView, \
    LogInView, SignUpView, LogOutView, LoggedUserHomePageView


urlpatterns = [
    path('', MainPageView.as_view(), name="main"),
    path('vacancies', VacanciesView.as_view(), name="vacancies"),
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LogInView.as_view(), name='login'),
    path('logout', LogOutView.as_view(), name='logout'),
    path('home', LoggedUserHomePageView.as_view(), name='home'),
    path('vacancy/new', LoggedUserHomePageView.as_view(), name='vacancy_new'),
]
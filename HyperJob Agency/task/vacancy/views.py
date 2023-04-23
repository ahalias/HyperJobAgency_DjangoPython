from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView


from .models import Vacancy
from resume.models import Resume
from .forms import AddForm



def save_form(request, model_type):
    form = AddForm(request.POST)
    if form.is_valid():
        instance = model_type(
            author=request.user,
            description=form.cleaned_data['description'],
        )
        instance.save()
        return redirect('home')

class LoggedUserHomePageView(View):

    def dispatch(self, request, *args, **kwargs):
        if 'vacancy/new' in request.path and not request.user.is_staff:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        if request.user.is_staff or request.user.is_authenticated:
            form = AddForm()
        else:
            form = None
        return render(request, "home.html", {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            form = save_form(request, Resume)
        else:
            form = None
        return render(request, "home.html", {'form': form})


class MainPageView(View):

    def get(self, request):
        return render(request, 'index.html')

class VacanciesView(View):

    def get(self, request):
        vacancies = Vacancy.objects.all()
        return render(request, "vacancies.html", {'vacancies': vacancies})

class LogOutView(LogoutView):
    template_name = 'logout.html'
    success_url = reverse_lazy('main')

    def get_success_url(self):
        return self.success_url

class LogInView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('main')

    def get_success_url(self):
        return self.success_url


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")
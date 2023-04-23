from django.shortcuts import render
from django.views import View

from .models import Resume
# Create your views here.


class ResumesView(View):

    def get(self, request):
        resumes = Resume.objects.all()
        return render(request, "resumes.html", {'resumes': resumes})

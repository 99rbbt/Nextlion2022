from django.shortcuts import render

from subjectApp.models import Major
from .models import Major
from django.views.generic import CreateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy
# Create your views here.

class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()

    return render(request, 'home.html', {'majors' : majors, 'subjects' : subjects})

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

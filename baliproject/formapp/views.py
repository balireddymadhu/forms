from django.http import HttpResponse
from django.shortcuts import render

from . import forms
from . forms import StudentForm


def college(arg):

    return HttpResponse (arg)


def student(request):
    form = forms.StudentForm()
    if request.method=='POST':
        form = forms.StudentForm(request.POST)
        print("well")
        if form.is_valid():
            print("Form validateon success")
            print("Name:",form.cleaned_data['name'])
            print("Rollno:", form.cleaned_data['rollno'])
            print("Email:", form.cleaned_data['email'])
            print("Feedback:",form.cleaned_data['feedback'])



    return render(request,"home.html",{'form':form})


# Create your views here.

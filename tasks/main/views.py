# views.py
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="New Task")
#Create your views here
def mainList(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, 'main/mainList.html', {
        "tasks": request.session["tasks"]
    })


def mainForm(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["tasks"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:mainList"))
        else:
            return render(request, "main/mainForm.html", {
                "form": form
            })
        
    return render(request, "main/mainForm.html", {
        "form":  NewTaskForm()
    })

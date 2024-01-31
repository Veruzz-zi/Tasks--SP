# views.py
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def mainForm(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:mainList"))
        else:
            return render(request, "main/mainForm.html", {
                "form": form
            })
        
    return render(request, "main/mainForm.html", {
        "form":  NewTaskForm()
    })


def mainList(request):
    return render(request, 'main/mainList.html', {
        "tasks": tasks
    })

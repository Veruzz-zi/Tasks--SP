from django.shortcuts import render

# Create your views here.
def mainForm(request):
    return render(request, 'main/mainForm.html')


def mainList(request):
    return render(request, 'main/mainList.html')

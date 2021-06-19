from django.shortcuts import render
from .models import todoModel
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, "mytodo/index.html", {"todo": todoModel.objects.all()})

def getTask(request):
    if request.method == "POST":
        o=todoModel(todo=request.POST.get("add"), date=request.POST.get("date"))
        o.save()
        return HttpResponseRedirect(reverse("add"))


def deleteTask(request, a):
    todoModel.objects.get(id=a).delete()
    return HttpResponseRedirect(reverse("index"))



def add(request):
    return render(request, "mytodo/add.html")
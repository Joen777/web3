from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Comment
from django.views.decorators.csrf import csrf_protect

def home(request):#Вывод таблицы с базы даных
    comment = Comment.objects.all()
    return render(request, "index.html", {"comment": comment})



@csrf_protect
def create(request):
    if request.method == "POST":
        comment = Comment()
        comment.name = request.POST.get("name")
        comment.tittle = request.POST.get("tittle")
        comment.save()
    return HttpResponseRedirect("/")


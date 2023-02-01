from django.shortcuts import render
from new.models import table


def home(request):
    people = table.objects.all()
    return render(request, "index.html", {"people": people})

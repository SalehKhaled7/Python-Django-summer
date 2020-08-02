import json

from django.shortcuts import render


# Create your views here.
def index(request):
    text = "car page"
    context = {'text': text}
    return render(request, 'buy.html', context)



from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, 'app.html', {'user': request.user})
    if request.user.is_authenticated:
        return render(request, 'app.html', {'user': request.user})
    else:
        return HttpResponseRedirect('/')

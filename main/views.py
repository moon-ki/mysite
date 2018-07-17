from django.shortcuts import render

# Create your views here.


def index(request):
    # if request.session['authuser'] is None:
    #     request.session['authuser']=None
    return render(request, 'main/index.html')

def error(request):
    return render(request, 'main/error.html')
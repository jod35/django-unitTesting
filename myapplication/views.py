from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'myapplication/index.html')


def about(request):
    return render(request,'myapplication/about.html')
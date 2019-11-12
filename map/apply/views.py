from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pages/index.html')

def over(request):
    return render(request, 'pages/overlays.html')
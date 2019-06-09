from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'my_portfolio/home.html' )



def about(request):
    return render (request, 'my_portfolio/about.html' )



def work(request):
    return render (request, 'my_portfolio/work.html' )

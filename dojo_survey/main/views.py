from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def results(request):
     return render(request, 'results.html')

def direct_to_index(request):
    print("I'm going home!")
    return redirect('/')

